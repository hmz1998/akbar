from django.db import models
from django.utils.translation import ugettext_lazy as _
from painless.utils.models.common import TimeStampModelMixin, ImageModelMixin


class ChooseUs(TimeStampModelMixin, ImageModelMixin):
    id = models.BigAutoField(primary_key=True)

    title = models.CharField(
        _("عنوان"),
        max_length=100,
    )

    description = models.TextField(
        verbose_name="توضیحات",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("انتخاب‌ما")
        verbose_name_plural = _("انتخاب‌ما")
