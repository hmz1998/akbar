from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'pages/index.html'
    page_name = "خانه"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        return context
