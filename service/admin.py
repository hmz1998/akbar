from django.contrib import admin

# Register your models here.
from sorl.thumbnail.admin import AdminImageMixin

from service.models import Service, ProjectsCategory, Project, ProjectGallery, BlogCategory, Blog


@admin.register(Service)
class ServiceAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('created',)
    search_fields = ('title', 'description')
    ordering = ('-created',)


@admin.register(ProjectsCategory)
class ProjectsCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('created',)
    search_fields = ('title',)
    ordering = ('-created',)


class ProjectGalleryInlineAdmin(admin.TabularInline, AdminImageMixin):
    model = ProjectGallery
    can_delete = True
    extra = 1
    classes = ['collapse']
    fk_name = 'project'
    verbose_name = "عکس"
    verbose_name_plural = "گالری"


@admin.register(Project)
class ProjectAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('created',)
    search_fields = ('title', 'description')
    ordering = ('-created',)

    filter_horizontal = ('categories',)

    inlines = [
        ProjectGalleryInlineAdmin,
    ]


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass
