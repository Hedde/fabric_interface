__author__ = 'heddevanderheide'

# Django specific
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'fabric_interface/home.html'