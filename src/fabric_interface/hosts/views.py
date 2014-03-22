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
from viewsets import ModelViewSet, SLUG


class HostDetailView(DetailView):
    def get_context_data(self, **kwargs):
        context = super(HostDetailView, self).get_context_data(**kwargs)
        context.update({
            'title': _(u"View"),
            'action': 'view'
        })
        return context


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


class HostDeleteView(DeleteView):
    success_url = reverse_lazy('host_index')

    def get_context_data(self, **kwargs):
        context = super(HostDeleteView, self).get_context_data(**kwargs)
        context.update({
            'title': _(u"Delete"),
            'action': 'delete'
        })
        return context

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