import json

import requests
from django.conf import settings


class SendSms:
    def __init__(self, account_id, auth_token, *args, **kwargs):
        self.url = "https://RestfulSms.com/"

        self.user_api_key = account_id
        self.secret_key = auth_token

        self.headers = {
            'Content-Type': 'application/json'
        }

        self.__secret_payload = {
            "UserApiKey": self.user_api_key,
            "SecretKey": self.secret_key
        }

    def __security_token(self, *args, **kwargs):
        url = self.url + 'api/Token'
        payload = json.dumps(self.__secret_payload)

        response = requests.request("POST", url, headers=self.headers, data=payload)
        response = json.loads(response.text)

        if response.get('IsSuccessful'):
            return response.get('TokenKey'), True
        else:
            return None, False

    def send_sms(self, to, message):
        security_token, successful = self.__security_token()
        url = self.url + 'api/MessageSend'

        if successful:
            payload = json.dumps({
                "Messages": [message],
                "MobileNumbers": [to],
                "LineNumber": settings.SMS_LINE_NUMBER,
                "SendDateTime": "",
                "CanContinueInCaseOfError": "false",
            })
            headers = {
                'Content-Type': 'application/json',
                'x-sms-ir-secure-token': security_token
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            response = json.loads(response.text)
            if response.get('IsSuccessful'):
                return response.get('message'), True
            else:
                return 'Sms does not send successfully.', False
        else:
            return 'Security Token Failed.', False


send = SendSms(settings.SMS_USER_API_KEY, settings.SMS_SECRET_KEY)
