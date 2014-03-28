__author__ = 'heddevanderheide'

# Django specific
from django.views.generic import TemplateView

# App specific
from fabric_interface.formulae.models import FormulaPosition


class FormulaeView(TemplateView):
    template_name = 'formulae/develop.html'

    def get_context_data(self, **kwargs):
        context = super(FormulaeView, self).get_context_data(**kwargs)
        context['trees'] = FormulaPosition.objects.filter(parent__isnull=True)
        return context