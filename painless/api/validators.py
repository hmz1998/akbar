from django.contrib.auth import get_user_model
from rest_framework import serializers


class PhoneNumberExistenceCheck:
    def __init__(self, base):
        self.base = base

    def __call__(self, value):
        queryset = get_user_model().objects.filter(useame=value)
        if queryset.exists():
            message = 'User is Exists.' % self.base
            raise serializers.ValidationError(message)
