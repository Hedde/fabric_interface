__author__ = 'heddevanderheide'

# Django specific
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

# App specific
from viewsets import ModelViewSet


class HostCreateView(CreateView):
    success_url = reverse_lazy('host_index')


class HostViewSet(ModelViewSet):
    def __init__(self, *args, **kwargs):
        self.views[b'create_view']['view'] = HostCreateView
        super(HostViewSet, self).__init__(*args, **kwargs)