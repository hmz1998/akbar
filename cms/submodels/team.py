from django.db import models
from django.utils.translation import ugettext_lazy as _

from painless.utils.models.common import TimeStampModelMixin, ImageModelMixin


class Founder(TimeStampModelMixin, ImageModelMixin):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(
        _("نام"),
        max_length=100,
    )

    is_index = models.BooleanField(
        _("نمایش در صفحه اصلی")
    )

    job = models.CharField(
        _("سمت"),
        max_length=100,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("بنیانگذار")
        verbose_name_plural = _("بنیانگذاران")
