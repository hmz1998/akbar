from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.submodels.team import Founder
from painless.utils.models.common import TimeStampModelMixin, ImageModelMixin


class Brand(TimeStampModelMixin, ImageModelMixin):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(
        _("نام"),
        max_length=50,
        validators=[
            MinLengthValidator(3)
        ]
    )

    link = models.URLField(
        _("پیوند (لینک)")
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("برند")
        verbose_name_plural = _("برندها")
