from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.submodels.team import Founder
from painless.utils.models.common import TimeStampModelMixin


class Social(TimeStampModelMixin):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(
        _("عنوان"),
        max_length=50,
        validators=[
            MinLengthValidator(3)
        ]
    )

    founder = models.ForeignKey(
        Founder,
        on_delete=models.CASCADE,
        related_name='socials',
        verbose_name="بنیانگذار",
        null=True,
        blank=True
    )

    link = models.URLField(
        _("پیوند (لینک)")
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("شبکه اجتماعی")
        verbose_name_plural = _("شبکه‌های اجتماعی")
