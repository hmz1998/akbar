from django.urls import path, re_path, include
from rest_framework import routers

from cms.api.views import (
    ContactView, NewsletterUserView,
)

router = routers.SimpleRouter()
router.register(r'contact', ContactView)
router.register(r'newsletter/subscribe', NewsletterUserView)

urlpatterns = router.urls

urlpatterns += []
