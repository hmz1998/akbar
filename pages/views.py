from django.views.generic import TemplateView

from cms.submodels.about import About
from cms.submodels.brand import Brand
from cms.submodels.offer import Offer
from cms.submodels.setting import Setting
from cms.submodels.slider import Slider
from cms.submodels.social import Social
from cms.submodels.support import Support
from cms.submodels.team import Founder
from cms.submodels.why_choose_us import ChooseUs


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

        return context
