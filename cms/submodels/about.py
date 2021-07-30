from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import (
    FileExtensionValidator
)

from painless.utils.models.common import TimeStampModelMixin, ImageModelMixin, VideoModelMixin


class About(TimeStampModelMixin, ImageModelMixin, VideoModelMixin):
    id = models.BigAutoField(primary_key=True)

    experience = models.PositiveSmallIntegerField(
        _("تجربه کاری"),
    )
    description = models.TextField(
        _("توضیحات")
    )

    def __str__(self):
        return f'درباره‌ما {self.id}'

    class Meta:
        verbose_name = _("درباره‌ما")
        verbose_name_plural = _("درباره‌ما")
