import secrets
import json
import random
from _datetime import timedelta

from django.conf import settings

from rest_framework import status
from rest_framework.exceptions import ValidationError

from django.utils.translation import ugettext_lazy as _

from painless.otp.ippanel import sms
from users.tasks import expire_token
from users.models import OTPHistory
from painless.otp.iran_otp import iran_otp


class OTP_Token_API:
    def __init__(self, phone_number, scope, *args, **kwargs):
        self.token_existence_message = kwargs.get('token_existence_message', _("Token already is sent. Please use it."))
        self.send_sms_message = kwargs.get('send_sms_message',
                                           _("An sms is sent to your phone number. Please add sent code to text box."))

        self.phone_number = phone_number
        self.scope = scope

    def generate(self, max_size):
        return ''.join(random.sample('123456789', max_size))

    def get_instance(self):
        return OTPHistory.objects.filter(phone_number=self.phone_number, is_active=True, scope=self.scope).first()

    def __check_token_existence(self):
        otp_obj = OTPHistory.objects.filter(phone_number=self.phone_number, is_active=True, scope=self.scope)
        return otp_obj.exists()

    def __create(self):
        otp = OTPHistory.objects.create(
            phone_number=self.phone_number,
            scope=self.scope,
            token=self.generate(5)
        )
        return otp

    def __schedule(self, otp_obj):
        expire_token(otp_obj)

    def __send_sms(self, otp=None):
        token = otp.token
        if token:
            pattern_values = {
                "code": token,
            }
        else:
            pattern_values = {
                "code": self.generate(6),
            }
        if otp.scope == 'l':
            send = sms.send_pattern(
                settings.IPPANEL_LOGIN_TEMPLATE,
                settings.IPPANEL_SERVICE_NUMBER,
                self.phone_number,
                pattern_values,
            )
        elif otp.scope == 'r':
            send = sms.send_pattern(
                settings.IPPANEL_REGISTER_TEMPLATE,
                settings.IPPANEL_SERVICE_NUMBER,
                self.phone_number,
                pattern_values,
            )
        else:
            send = None

        return send

    def send_otp(self):

        if self.__check_token_existence():
            message = self.token_existence_message
            code = status.HTTP_403_FORBIDDEN

        else:
            otp = self.__create()
            send = self.__send_sms(otp=otp)
            if send:
                message = self.send_sms_message
                code = status.HTTP_201_CREATED
                self.__schedule(otp.pk)
            else:
                message = 'Bad Request'
                code = status.HTTP_400_BAD_REQUEST

        return message, code

    def verify_otp(self, token):
        otp_obj = OTPHistory.objects.filter(phone_number=self.phone_number, is_active=True, scope=self.scope)
        if not otp_obj.exists():
            return False

        otp_obj = otp_obj.first()

        if not token == otp_obj.token:
            return False

        return True
