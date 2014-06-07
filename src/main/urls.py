from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, FormView
from fabric_interface.formulae.forms import FabfileForm
from fabric_interface.formulae.models import Fabfile

__author__ = 'heddevanderheide'

# Django specific
from django.conf.urls import patterns, include, url


class X(FormView):
    form_class = FabfileForm
    success_url = reverse_lazy('test')
    template_name = 'fabric_interface/test.html'

    def get_context_data(self, **kwargs):
        context = super(X, self).get_context_data(**kwargs)
        context['object_list'] = Fabfile.objects.all()
        return context

    def form_valid(self, form):
        return super(X, self).form_valid(form)

    def form_invalid(self, form):
        return super(X, self).form_invalid(form)



urlpatterns = patterns('',
    url('^test/', X.as_view(), name='test'),
    url('', include('fabric_interface.urls'))
)