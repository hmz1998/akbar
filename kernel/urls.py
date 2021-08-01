"""kernel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    re_path(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    re_path(r'^secret/', admin.site.urls),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^', include('pages.urls')),
    re_path(r'^', include('cms.urls')),
]

admin.site.site_header = 'پنل مدیریت اکبر'

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
