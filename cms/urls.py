from django.urls import path, re_path, include

urlpatterns = [
    path('api/', include('cms.api.urls')),
]
