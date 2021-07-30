from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from painless.utils.models.common import TimeStampModelMixin


class Faq(TimeStampModelMixin):
    question = models.CharField(
        _("متن سوال"),
        max_length=80,
        validators=[
            MaxLengthValidator(80),
            MinLengthValidator(5),
        ],
    )

    answer = models.TextField(
        _("پاسخ"),
    )

    class Meta:
        verbose_name = _("سوال")
        verbose_name_plural = _("سوالات متداول")

    def __str__(self):
        return self.question
