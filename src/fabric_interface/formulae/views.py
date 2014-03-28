__author__ = 'heddevanderheide'

# Django specific
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

# App specific
from fabric_interface.formulae.forms import FormulaPositionForm
from fabric_interface.formulae.models import FormulaPosition


class FormulaeView(CreateView):
    form_class = FormulaPositionForm
    success_url = reverse_lazy('test')
    template_name = 'formulae/test.html'

    def get_context_data(self, **kwargs):
        context = super(FormulaeView, self).get_context_data(**kwargs)
        context['trees'] = FormulaPosition.objects.filter(parent__isnull=True)
        return context