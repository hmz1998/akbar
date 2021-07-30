from django.conf import settings
from ippanel import Client

# you api key that generated from panel
api_key = settings.IPPANEL_API_KEY

# create client instance
sms = Client(api_key)
