__author__ = 'heddevanderheide'

# Django specific
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy, reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import (
    CreateView, UpdateView
)
# App specific
from fabric_interface.hosts.models import Host
from viewsets import ModelViewSet, SLUG


class HostCreateView(CreateView):
    success_url = reverse_lazy('host_index')

    def get_context_data(self, **kwargs):
        context = super(HostCreateView, self).get_context_data(**kwargs)
        context.update({
            'title': _(u"Create"),
            'action': 'create'
        })
        return context

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, _(u"Created {model} '{slug}' succesfully.".format(
                model=self.model._meta.verbose_name,
                slug=self.object.slug
            ))
        )
        return reverse('host_detail', kwargs={'slug': self.object.slug})


class HostUpdateView(UpdateView):
    success_url = reverse_lazy('host_index')

    def get_context_data(self, **kwargs):
        context = super(HostUpdateView, self).get_context_data(**kwargs)
        context.update({
            'title': _(u"Update"),
            'action': 'update'
        })
        return context

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, _(u"Updated {model} '{slug}' succesfully.".format(
                model=self.model._meta.verbose_name,
                slug=self.object.slug
            ))
        )
        return reverse('host_detail', kwargs={'slug': self.object.slug})


class HostViewSet(ModelViewSet):
    model = Host
    id_pattern = SLUG

    def __init__(self, *args, **kwargs):
        self.views[b'create_view']['view'] = HostCreateView
        self.views[b'update_view']['view'] = HostUpdateView
        super(HostViewSet, self).__init__(*args, **kwargs)