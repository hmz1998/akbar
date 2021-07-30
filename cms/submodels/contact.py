from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from painless.utils.models.common import TimeStampModelMixin
from painless.utils.regex.patterns import PERSIAN_PHONE_NUMBER_PATTERN


class Contact(TimeStampModelMixin):
    id = models.BigAutoField(primary_key=True)
    
    name = models.CharField(
        _("نام"),
        max_length=25,
        validators=[
            MinLengthValidator(3)
        ]
    )

    phone_number = models.CharField(
        _("شماره تماس"),
        max_length=13,
        validators=[
            MinLengthValidator(11),
            RegexValidator(
                PERSIAN_PHONE_NUMBER_PATTERN,
                message=_("شماره تلفن باید بصورت ‍‍‍‍‍ '+989123334444' و یا '09123334444' باشد."),
            )
        ]
    )

    message = models.CharField(
        _("پیام"),
        max_length=1000,
        validators=[
            MinLengthValidator(10)
        ]
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("تماس")
        verbose_name_plural = _("تماس ها")
