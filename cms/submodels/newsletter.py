from django.db import models
from django.utils.translation import ugettext_lazy as _

from painless.utils.models.common import TimeStampModelMixin


class NewsletterUser(TimeStampModelMixin):
    id = models.BigAutoField(primary_key=True)

    email = models.EmailField(
        _("ایمیل"),
        max_length=255,
    )

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("عضو خبرنامه")
        verbose_name_plural = _("اعضای خبرنامه")
