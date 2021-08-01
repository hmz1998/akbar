from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin

from cms.models import (
    About,
    Setting,
    Slider,
    Social,
    Brand,
    Contact,
    Faq,
    Offer,
    Support,
    Founder,
    ChooseUs,
)
from cms.submodels.newsletter import NewsletterUser


@admin.register(Setting)
class SettingAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('domain', 'name', 'title', 'phone_number', 'email')
    list_filter = ('created',)
    search_fields = ('domain', 'name', 'title')
    ordering = ('-created',)


@admin.register(About)
class AboutAdmin(AdminImageMixin, admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')
    list_filter = ('created',)
    search_fields = ('name', 'phone_number', 'message')
    ordering = ('-created',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(NewsletterUser)
class NewsletterUserAdmin(admin.ModelAdmin):
    list_display = ('email',)
    list_filter = ('created',)
    search_fields = ('email',)
    ordering = ('-created',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    pass


@admin.register(Slider)
class SliderAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('title', 'is_active',)
    list_filter = ('created', 'is_active')
    search_fields = ('title',)
    ordering = ('-created',)


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'discount', 'is_active')
    list_filter = ('created', 'is_active',)
    search_fields = ('title', 'description')
    ordering = ('-created',)

    list_editable = ('is_active', 'discount')


@admin.register(ChooseUs)
class ChooseUsAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('title', 'created')
    list_filter = ('created',)
    search_fields = ('title', 'description')
    ordering = ('-created',)


@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    list_filter = ('created',)
    search_fields = ('title', 'description')
    ordering = ('-created',)


class SocialInlineAdmin(admin.TabularInline, AdminImageMixin):
    model = Social
    can_delete = True
    extra = 1
    classes = ['collapse']
    fk_name = 'founder'
    verbose_name = "شبکه مجازی"
    verbose_name_plural = "شبکه‌های مجازی"


@admin.register(Founder)
class FounderAdmin(admin.ModelAdmin):
    list_display = ('name', 'job', 'is_index')
    list_filter = ('created', 'is_index')
    search_fields = ('title', 'job')
    ordering = ('-created',)

    list_editable = ('is_index',)

    inlines = [
        SocialInlineAdmin,
    ]


@admin.register(Brand)
class BrandAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('name', 'link', 'created')
    list_filter = ('created',)
    search_fields = ('name',)
    ordering = ('-created',)


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    list_filter = ('created',)
    search_fields = ('question', 'answer')
    ordering = ('-created',)
