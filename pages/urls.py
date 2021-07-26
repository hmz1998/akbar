from django.urls import path, re_path, include

from pages.views import HomeView

app_name = 'pages'
urlpatterns = [
    re_path(r'^$', HomeView.as_view(), name='home'),
]
