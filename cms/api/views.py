from rest_framework.response import Response
from rest_framework.viewsets import (
    GenericViewSet,
)
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin
)

from cms.api.serializers import (
    ContactSerializer, NewsletterUserSerializer,
)
from cms.submodels.contact import Contact
from cms.submodels.newsletter import NewsletterUser


class ContactView(CreateModelMixin, GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class NewsletterUserView(CreateModelMixin, GenericViewSet):
    queryset = NewsletterUser.objects.all()
    serializer_class = NewsletterUserSerializer
