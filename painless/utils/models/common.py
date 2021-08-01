import secrets
import uuid

from django.db import models

from django.core.validators import (
    FileExtensionValidator,
    MinLengthValidator,
    MaxLengthValidator
)

from sorl.thumbnail import ImageField

from django.utils.translation import ugettext_lazy as _

from painless.utils.upload.path import date_directory_path


class UUIDBaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True


class SKUMixin(models.Model):
    sku = models.CharField(
        max_length=255,
        editable=False,
        unique=True,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class TitleSlugLinkModelMixin(models.Model):
    title = models.CharField(
        _("Title"),
        max_length=150,
        validators=[
            MaxLengthValidator(150),
            MinLengthValidator(3)
        ],
        unique=True
    )
    slug = models.SlugField(
        _("Slug"),
        editable=False,
        allow_unicode=True,
        max_length=150,
        unique=True
    )

    class Meta:
        abstract = True


class TimeStampModelMixin(models.Model):
    created = models.DateTimeField(_("زمان ایجاد"), auto_now_add=True)
    modified = models.DateTimeField(_("زمان ویرایش"), auto_now=True)

    class Meta:
        abstract = True


class ImageModelMixin(models.Model):
    picture = ImageField(
        _("عکس"),
        upload_to=date_directory_path,
        height_field='height_field',
        width_field='width_field',
        max_length=110,
        validators=[FileExtensionValidator(allowed_extensions=['JPG', 'JPEG', 'PNG', 'jpg', 'jpeg', 'png'])],
        null=True, blank=True
    )

    picture_alternate_text = models.CharField(
        _("توضیحات عکس"),
        max_length=110,
        validators=[
            MaxLengthValidator(150),
            MinLengthValidator(3)
        ],
        null=True, blank=True
    )
    width_field = models.PositiveSmallIntegerField(
        _("Width Field"),
        editable=False,
        null=True, blank=True
    )
    height_field = models.PositiveSmallIntegerField(
        _("Height Field"),
        editable=False,
        null=True, blank=True
    )

    class Meta:
        abstract = True


class VideoModelMixin(models.Model):
    video = models.FileField(
        _("ویدیو"),
        upload_to=date_directory_path,
        max_length=110,
        validators=[
            FileExtensionValidator(allowed_extensions=['mp4', ])
        ],
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class LogoModelMixin(models.Model):
    logo = ImageField(
        _("لوگو"),
        upload_to=date_directory_path,
        height_field='logo_width_field',
        width_field='logo_height_field',
        max_length=110,
        validators=[FileExtensionValidator(allowed_extensions=['JPG', 'JPEG', 'PNG', 'jpg', 'jpeg', 'png'])],
        help_text="فرمت لوگو فقظ png میتواند باشد."
    )

    logo_alternate_text = models.CharField(
        _("توضیحات لوگو"),
        max_length=110,
        validators=[
            MinLengthValidator(3)
        ]
    )
    logo_width_field = models.PositiveSmallIntegerField(_("Logo Width Field"), editable=False)
    logo_height_field = models.PositiveSmallIntegerField(_("Logo Height Field"), editable=False)

    class Meta:
        abstract = True


class SVGModelMixin(models.Model):
    svg = models.FileField(
        _("آیکن (SVG)"),
        upload_to=date_directory_path,
        max_length=110,
        help_text='فرمت فایل باید svg باشد',
        validators=[FileExtensionValidator(allowed_extensions=['svg', 'SVG', ])],
        null=True,
        blank=True
    )

    svg_alt_text = models.CharField(
        _("توضیحات آیکن"),
        max_length=110,
        validators=[
            MaxLengthValidator(150),
            MinLengthValidator(3)
        ],
        null=True,
        blank=True
    )

    class Meta:
        abstract = True
