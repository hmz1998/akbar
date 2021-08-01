import secrets

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from painless.utils.models.common import TimeStampModelMixin, ImageModelMixin, TitleSlugLinkModelMixin, SKUMixin


class Service(TimeStampModelMixin, ImageModelMixin, TitleSlugLinkModelMixin):
    summary = models.TextField(
        verbose_name="توضیحات مختصر",
    )

    description = RichTextUploadingField(
        verbose_name="توضیحات",
    )

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Service, self).save(**kwargs)

    def get_absolute_url(self):
        return reverse('pages:service', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "سرویس"
        verbose_name_plural = "سرویس ها"


class ProjectsCategory(TimeStampModelMixin, TitleSlugLinkModelMixin, SKUMixin):

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        if not self.sku:
            self.sku = 'PC-' + secrets.token_urlsafe(3)
        self.slug = slugify(self.title, allow_unicode=True)
        super(ProjectsCategory, self).save(**kwargs)

    def get_absolute_url(self):
        return reverse('pages:projects_category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "دسته‌بندی پروژه"
        verbose_name_plural = "دسته‌بندی های پروژه"


class Project(TimeStampModelMixin, TitleSlugLinkModelMixin, ImageModelMixin):
    categories = models.ManyToManyField(
        ProjectsCategory,
        related_name='projects',
        verbose_name="دسته‌بندی ها",
    )

    client = models.CharField(
        verbose_name="کارفرما",
        max_length=50,
    )

    start_date = models.DateField(
        verbose_name="تاریخ شروع"
    )

    end_date = models.DateField(
        verbose_name="تاریخ پایان"
    )

    price = models.CharField(
        max_length=15,
        verbose_name="قیمت"
    )

    location = models.CharField(
        max_length=100,
        verbose_name="آدرس پروژه"
    )

    summary = models.TextField(
        verbose_name="درباره پروژه",
        max_length=500
    )

    description = RichTextUploadingField(
        verbose_name="توضیحات",
    )

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Project, self).save(**kwargs)

    def get_absolute_url(self):
        return reverse('pages:project', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه ها"


class ProjectGallery(TimeStampModelMixin, ImageModelMixin):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        verbose_name='پروژه',
        related_name='galleries'
    )

    def __str__(self):
        return self.project.title

    class Meta:
        verbose_name = "عکس پروژه"
        verbose_name_plural = "عکس‌های پروژه"


class BlogCategory(TimeStampModelMixin, TitleSlugLinkModelMixin):

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(BlogCategory, self).save(**kwargs)

    def get_absolute_url(self):
        return reverse('pages:blogs_category', kwargs={'slug': self.slug, 'page': 1})

    class Meta:
        verbose_name = "دسته‌بندی مطالب"
        verbose_name_plural = "دسته‌بندی های مطالب"


class Blog(TitleSlugLinkModelMixin, TimeStampModelMixin, ImageModelMixin):
    category = models.ForeignKey(
        BlogCategory,
        on_delete=models.CASCADE,
        related_name='blogs',
        verbose_name='دسته‌بندی'
    )

    summary = models.TextField(
        verbose_name="توضیحات مختصر",
    )

    description = RichTextUploadingField(
        verbose_name="توضیحات",
    )

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Blog, self).save(**kwargs)

    def get_absolute_url(self):
        return reverse('pages:blog', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "مطلب"
        verbose_name_plural = "مطالب"
