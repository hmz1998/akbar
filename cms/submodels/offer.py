from django.db import models
from django.utils.translation import ugettext_lazy as _
from painless.utils.models.common import TimeStampModelMixin, ImageModelMixin


class Offer(TimeStampModelMixin, ImageModelMixin):
    id = models.BigAutoField(primary_key=True)

    title = models.CharField(
        _("عنوان"),
        max_length=100,
    )

    discount = models.PositiveSmallIntegerField(
        _("تخفیف")
    )

    description = models.TextField(
        verbose_name="توضیحات",
    )

    is_active = models.BooleanField(
        _("فعال (باشد/نباشد)"),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("پیشنهاد")
        verbose_name_plural = _("پیشنهادات")
