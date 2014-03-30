__author__ = 'heddevanderheide'

# Django specific
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    CreateView, UpdateView
)

# App specific
from fabric_interface.formulae.forms import FormulaForm
from fabric_interface.formulae.models import FormulaPosition, Formula


class FormulaCreateView(CreateView):
    form_class = FormulaForm
    success_url = reverse_lazy('test')
    template_name = 'formulae/test.html'

    def get_context_data(self, **kwargs):
        context = super(FormulaCreateView, self).get_context_data(**kwargs)
        context['trees'] = FormulaPosition.objects.filter(parent__isnull=True)
        return context


class FormulaUpdateView(UpdateView):
    model = Formula
    form_class = FormulaForm
    template_name = 'formulae/test.html'

    def get_success_url(self):
        return reverse_lazy('formula_update', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(FormulaUpdateView, self).get_context_data(**kwargs)
        context['trees'] = FormulaPosition.objects.filter(parent__isnull=True)
        return context