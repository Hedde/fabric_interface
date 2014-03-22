__author__ = 'heddevanderheide'

# Django specific
from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _


class HomeView(TemplateView):
    template_name = 'fabric_interface/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
            'title': _(u"Home"),
            'action': 'view'
        })
        return context