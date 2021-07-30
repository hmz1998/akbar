from django.db import models
from django.utils.translation import ugettext_lazy as _
from painless.utils.models.common import TimeStampModelMixin, ImageModelMixin


class Support(TimeStampModelMixin):
    id = models.BigAutoField(primary_key=True)

    title = models.CharField(
        _("عنوان"),
        max_length=100,
    )

    icon = models.CharField(
        _("ایکن"),
        max_length=200,
    )

    description = models.TextField(
        verbose_name="توضیحات",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("خدمت")
        verbose_name_plural = _("خدمات")
