from django.contrib.gis.geos import Point
from django.db import models
from django.utils.translation import ugettext_lazy as _
from location_field.models.plain import PlainLocationField
from django.core.validators import (
    MinLengthValidator,
    RegexValidator
)

from painless.utils.models.common import (
    TimeStampModelMixin,
    LogoModelMixin
)
from painless.utils.regex.patterns import PERSIAN_PHONE_NUMBER_PATTERN


class Setting(TimeStampModelMixin, LogoModelMixin):
    id = models.BigAutoField(primary_key=True)
    domain = models.URLField(
        _("دامنه سایت"),
    )

    name = models.CharField(
        _("نام سایت"),
        max_length=125,
        validators=[
            MinLengthValidator(5)
        ]
    )

    title = models.CharField(
        _("عنوان سایت"),
        max_length=125,
        validators=[
            MinLengthValidator(5)
        ]
    )

    phone_number = models.CharField(
        _("شماره تلفن"),
        max_length=13,
        help_text=_("شماره تلفن باید بصورت ‍‍‍‍‍ '+989123334444' و یا '09123334444' باشد."),
        validators=[
            MinLengthValidator(11),
            RegexValidator(
                PERSIAN_PHONE_NUMBER_PATTERN,
                message=_("شماره تلفن باید بصورت ‍‍‍‍‍ '+989123334444' و یا '09123334444' باشد."),
            )
        ]
    )

    email = models.EmailField(
        _("ایمیل"),
        max_length=255
    )

    slogan = models.CharField(
        _("شعار"),
        max_length=255,
        validators=[
            MinLengthValidator(5)
        ]
    )

    address = models.CharField(
        _("آدرس"),
        max_length=255,
        validators=[
            MinLengthValidator(5)
        ]
    )

    city = models.CharField(
        _("شهر"),
        max_length=255,
        null=True,
        blank=True
    )

    location = PlainLocationField(
        based_fields=['city'],
        verbose_name=_("موقعیت مکانی"),
        zoom=7,
        default=Point(51.3896004, 35.6892523),
    )

    description = models.TextField(
        verbose_name="توضیحات"
    )

    time_table = models.CharField(
        verbose_name="ساعت کاری",
        max_length=300
    )

    enamad = models.TextField(
        _("نماد اعتماد"),
        null=True,
        blank=True
    )

    samandehi = models.TextField(
        _("نماد ساماندهی"),
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _("تنظیم")
        verbose_name_plural = _("تنظیمات")

    def __str__(self):
        return self.domain
