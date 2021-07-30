from rest_framework import serializers
from sorl.thumbnail import get_thumbnail
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)
from cms.submodels.contact import Contact
from cms.submodels.newsletter import NewsletterUser


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'phone_number', 'message']


class NewsletterUserSerializer(ModelSerializer):
    class Meta:
        model = NewsletterUser
        fields = ['email', ]
