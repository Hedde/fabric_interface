__author__ = 'heddevanderheide'

# Django specific
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import (
    DetailView, CreateView, UpdateView, DeleteView
)
# App specific
from fabric_interface.hosts.models import Host
from fabric_interface.mixins import (
    DetailContext, CreateContext, UpdateContext, DeleteContext
)
from viewsets import ModelViewSet, SLUG


class HostDetailView(DetailContext, DetailView):
    pass


class HostCreateView(CreateContext, CreateView):
    success_url = reverse_lazy('host_index')

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, _(u"Created {model} '{slug}' succesfully.".format(
                model=self.model._meta.verbose_name,
                slug=self.object.slug
            ))
        )
        return reverse('host_detail', kwargs={'slug': self.object.slug})


class HostUpdateView(UpdateContext, UpdateView):
    success_url = reverse_lazy('host_index')

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, _(u"Updated {model} '{slug}' succesfully.".format(
                model=self.model._meta.verbose_name,
                slug=self.object.slug
            ))
        )
        return reverse('host_detail', kwargs={'slug': self.object.slug})


class HostDeleteView(DeleteContext, DeleteView):
    success_url = reverse_lazy('host_index')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        messages.add_message(
            self.request, messages.SUCCESS, _(u"Deleted {model} '{slug}' succesfully.".format(
                model=self.model._meta.verbose_name,
                slug=self.object.slug
            ))
        )
        self.object.delete()
        return HttpResponseRedirect(success_url)


class HostViewSet(ModelViewSet):
    model = Host
    id_pattern = SLUG

    def __init__(self, *args, **kwargs):
        self.views[b'detail_view']['view'] = HostDetailView
        self.views[b'create_view']['view'] = HostCreateView
        self.views[b'update_view']['view'] = HostUpdateView
        self.views[b'delete_view']['view'] = HostDeleteView
        super(HostViewSet, self).__init__(*args, **kwargs)