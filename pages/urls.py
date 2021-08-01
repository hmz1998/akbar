from django.urls import path, re_path, include

from pages import views

app_name = 'pages'
urlpatterns = [
    re_path(r'^$', views.HomeView.as_view(), name='home'),
    re_path(r'^about/$', views.AboutView.as_view(), name='about'),
    re_path(r'^contact/$', views.ContactView.as_view(), name='contact'),
    re_path(r'^team/$', views.TeamView.as_view(), name='team'),
    re_path(r'^faq/$', views.FaqView.as_view(), name='faq'),
    re_path(r'^services/$', views.ServicesView.as_view(), name='services'),
    re_path(r'^projects/$', views.ProjectsView.as_view(), name='projects'),
    re_path(r'^projects/category/(?P<slug>[-\w]+)/$', views.CategoryProjectsView.as_view(), name='projects_category'),
    re_path(
        r'^blogs/category/(?P<slug>[-\w]+)/page/(?P<page>[\d]+)/$',
        views.CategoryBlogsView.as_view(),
        name='blogs_category'
    ),
    re_path(r'^blogs/$', views.BlogsView.as_view(), name='blogs'),
    re_path(
        r'^blogs/page/(?P<page>[\d]+)/$',
        views.BlogsView.as_view(),
        name='blogs'
    ),
    re_path(
        r'^service/(?P<slug>[-\w]+)/$',
        views.ServiceDetailView.as_view(),
        name='service'
    ),
    re_path(
        r'^project/(?P<slug>[-\w]+)/$',
        views.ProjectDetailView.as_view(),
        name='project'
    ),
    re_path(
        r'^blog/(?P<slug>[-\w]+)/$',
        views.BlogDetailView.as_view(),
        name='blog'
    ),
]
