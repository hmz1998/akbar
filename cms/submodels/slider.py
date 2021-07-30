from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import (
    FileExtensionValidator, MinLengthValidator, MaxLengthValidator
)

from painless.utils.models.common import TimeStampModelMixin, ImageModelMixin
from painless.utils.upload.path import date_directory_path
from sorl.thumbnail import ImageField


class Slider(TimeStampModelMixin, ImageModelMixin):
    id = models.BigAutoField(primary_key=True)
    sub_title = models.CharField(
        _("خوش آمدگویی"),
        max_length=100,
        validators=[
            MinLengthValidator(3)
        ],
        null=True,
        blank=True
    )

    title = models.TextField(
        _("عنوان"),
    )

    description = models.TextField(
        verbose_name="توضیحات",
    )

    is_active = models.BooleanField(
        _("فعال (باشد/نباشد)"),
    )

    btn = models.CharField(
        _("نام دکمه"),
        max_length=50,
        validators=[
            MinLengthValidator(3)
        ],
        null=True,
        blank=True
    )

    link = models.URLField(
        _("لینک"),
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("اسلایدر")
        verbose_name_plural = _("اسلایدرها")
