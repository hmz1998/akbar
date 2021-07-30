# from twilio.rest import Client
# from django.conf import settings
#
# class Twilio:
#
#     def __init__(self, account_sid, auth_token, *args, **kwargs):
#         self.client = Client(account_sid, auth_token)
#
#     def send_sms(self, to, body, from_=settings.TWILIO_DEFAULT_NUMBER):
#         message = self.client.messages.create(body=body, from_=from_, to=to)
#
# twilio = Twilio(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_ACCOUNT_TEST)