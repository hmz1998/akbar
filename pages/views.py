from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView

from cms.submodels.about import About
from cms.submodels.brand import Brand
from cms.submodels.faq import Faq
from cms.submodels.offer import Offer
from cms.submodels.setting import Setting
from cms.submodels.slider import Slider
from cms.submodels.social import Social
from cms.submodels.support import Support
from cms.submodels.team import Founder
from cms.submodels.why_choose_us import ChooseUs
from service.models import Service, Project, ProjectsCategory, BlogCategory, Blog


class HomeView(TemplateView):
    template_name = 'pages/index.html'
    page_name = "خانه"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['setting'] = Setting.objects.first()
        context['about'] = About.objects.first()
        context['sliders'] = Slider.objects.filter(is_active=True)
        context['socials'] = Social.objects.filter(founder=None)
        context['offer'] = Offer.objects.filter(is_active=True).first()
        context['choose_us'] = ChooseUs.objects.first()
        context['supports'] = Support.objects.all()[:4]
        context['founders'] = Founder.objects.filter(is_index=True)[:3]
        context['brands'] = Brand.objects.all()
        context['services'] = Service.objects.all()
        context['projects'] = Project.objects.all()[:12]
        context['projects_categories'] = ProjectsCategory.objects.all()
        context['blog_categories'] = BlogCategory.objects.all()
        context['blogs'] = Blog.objects.all()

        return context


class AboutView(TemplateView):
    template_name = 'pages/about.html'
    page_name = "درباره ما"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['setting'] = Setting.objects.first()
        context['about'] = About.objects.first()
        context['socials'] = Social.objects.filter(founder=None)
        context['offer'] = Offer.objects.filter(is_active=True).first()
        context['choose_us'] = ChooseUs.objects.first()
        context['supports'] = Support.objects.all()[:4]
        context['brands'] = Brand.objects.all()
        context['services'] = Service.objects.all()
        context['projects_categories'] = ProjectsCategory.objects.all()
        context['blog_categories'] = BlogCategory.objects.all()

        return context


class ContactView(TemplateView):
    template_name = 'pages/contact.html'
    page_name = "تماس باما"

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['setting'] = Setting.objects.first()
        context['socials'] = Social.objects.filter(founder=None)
        context['services'] = Service.objects.all()
        context['projects_categories'] = ProjectsCategory.objects.all()
        context['blog_categories'] = BlogCategory.objects.all()

        return context


class TeamView(TemplateView):
    template_name = 'pages/team.html'
    page_name = "تیم ما"

    def get_context_data(self, **kwargs):
        context = super(TeamView, self).get_context_data(**kwargs)
        context['setting'] = Setting.objects.first()
        context['socials'] = Social.objects.filter(founder=None)
        context['brands'] = Brand.objects.all()
        context['founders'] = Founder.objects.all()
        context['services'] = Service.objects.all()
        context['projects_categories'] = ProjectsCategory.objects.all()
        context['blog_categories'] = BlogCategory.objects.all()

        return context


class FaqView(TemplateView):
    template_name = 'pages/faqs.html'
    page_name = "سوالات متداول"

    def get_context_data(self, **kwargs):
        context = super(FaqView, self).get_context_data(**kwargs)
        context['setting'] = Setting.objects.first()
        context['socials'] = Social.objects.filter(founder=None)
        context['offer'] = Offer.objects.filter(is_active=True).first()
        context['faqs'] = Faq.objects.all()
        context['brands'] = Brand.objects.all()
        context['services'] = Service.objects.all()
        context['projects_categories'] = ProjectsCategory.objects.all()
        context['blog_categories'] = BlogCategory.objects.all()

        return context


class ServicesView(TemplateView):
    template_name = 'pages/services.html'
    page_name = "سرویس ها"

    def get_context_data(self, **kwargs):
        context = super(ServicesView, self).get_context_data(**kwargs)
        context['setting'] = Setting.objects.first()
        context['socials'] = Social.objects.filter(founder=None)
        context['brands'] = Brand.objects.all()
        context['services'] = Service.objects.all()
        context['projects_categories'] = ProjectsCategory.objects.all()
        context['blog_categories'] = BlogCategory.objects.all()

        return context


class ServiceDetailView(DetailView):
    queryset = Service.objects.all()
    model = Service
    template_name = 'pages/service-detail.html'

    page_name = 'سرویس ها'
    context_object_name = 'service'

    def get_context_data(self, **kwargs):
        context = super(ServiceDetailView, self).get_context_data(**kwargs)
        context['setting'] = Setting.objects.first()
        context['socials'] = Social.objects.filter(founder=None)
        context['brands'] = Brand.objects.all()
        context['services'] = Service.objects.all()
        context['projects_categories'] = ProjectsCategory.objects.all()
        context['blog_categories'] = BlogCategory.objects.all()

        return context


class ProjectsView(TemplateView):
    template_name = 'pages/projects.html'
    page_name = "پروژه‌ها"

    def get_context_data(self, **kwargs):
        context = super(ProjectsView, self).get_context_data(**kwargs)
        context['setting'] = Setting.objects.first()
        context['socials'] = Social.objects.filter(founder=None)
        context['brands'] = Brand.objects.all()
        context['services'] = Service.objects.all()
        context['projects'] = Project.objects.all()
        context['projects_categories'] = ProjectsCategory.objects.all()
        context['blog_categories'] = BlogCategory.objects.all()

        return context


class CategoryProjectsView(DetailView):
    queryset = ProjectsCategory.objects.all()
    model = ProjectsCategory
    template_name = 'pages/category-projects.html'
    page_name = "پروژه‌ها"

    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super(CategoryProjectsView, self).get_context_data(**kwargs)
        context['setting'] = Setting.objects.first()
        context['socials'] = Social.objects.filter(founder=None)
        context['brands'] = Brand.objects.all()
        context['services'] = Service.objects.all()
        context['projects_categories'] = ProjectsCategory.objects.all()
        context['blog_categories'] = BlogCategory.objects.all()

        return context


class ProjectDetailView(DetailView):
    queryset = Project.objects.all()
    model = Project
    template_name = 'pages/project-detail.html'

    page_name = 'پروژه‌ها'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['setting'] = Setting.objects.first()
        context['socials'] = Social.objects.filter(founder=None)
        context['brands'] = Brand.objects.all()
        context['services'] = Service.objects.all()
        context['projects_categories'] = ProjectsCategory.objects.all()
        context['blog_categories'] = BlogCategory.objects.all()

        return context


class BlogsView(ListView):
    queryset = Blog.objects.all()
    template_name = 'pages/blog.html'

    paginate_by = 5

    page_name = 'مطالب'
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super(BlogsView, self).get_context_data(**kwargs)
        context['setting'] = Setting.objects.first()
        context['socials'] = Social.objects.filter(founder=None)
        context['brands'] = Brand.objects.all()
        context['services'] = Service.objects.all()
        context['projects_categories'] = ProjectsCategory.objects.all()
        context['blog_categories'] = BlogCategory.objects.all()
        return context


class CategoryBlogsView(View):
    template_name = 'pages/category-blog.html'

    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = dict()
        context['setting'] = Setting.objects.first()
        context['socials'] = Social.objects.filter(founder=None)
        context['brands'] = Brand.objects.all()
        context['services'] = Service.objects.all()
        context['projects_categories'] = ProjectsCategory.objects.all()
        context['blog_categories'] = BlogCategory.objects.all()
        context['new_blogs'] = Blog.objects.all()
        return context

    def get(self, request, slug, page, *args, **kwargs):
        category = BlogCategory.objects.get(slug=slug)

        blogs = category.blogs.all().order_by("-created")

        paginator = Paginator(blogs, self.paginate_by)

        try:

            blogs = paginator.get_page(page)

        except PageNotAnInteger:

            blogs = paginator.get_page(1)

        except EmptyPage:

            blogs = paginator.page(paginator.num_pages)

        context = self.get_context_data()

        context['blogs'] = blogs
        context['category'] = category
        context['view'] = {'page_name': "مطالب"}

        return render(
            request,
            self.template_name,
            context
        )


class BlogDetailView(DetailView):
    queryset = Blog.objects.all()
    model = Blog
    template_name = 'pages/blog-detail.html'

    page_name = 'مطالب'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['setting'] = Setting.objects.first()
        context['socials'] = Social.objects.filter(founder=None)
        context['brands'] = Brand.objects.all()
        context['services'] = Service.objects.all()
        context['projects_categories'] = ProjectsCategory.objects.all()
        context['blog_categories'] = BlogCategory.objects.all()
        context['blogs'] = Blog.objects.all()[:5]

        return context
