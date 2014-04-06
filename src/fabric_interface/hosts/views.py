__author__ = 'heddevanderheide'

# Django specific
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.utils.datastructures import SortedDict
from django.utils.translation import ugettext_lazy as _
from django.views.generic import (
    DetailView, CreateView, UpdateView, DeleteView
)

# App specific
from fabric_interface.hosts.models import Host
from fabric_interface.mixins import (
    DetailContextMixin, CreateContextMixin, UpdateContextMixin, DeleteContextMixin
)
from fabric_interface.mixins import PermissionRequiredMixin
from fabric_interface.utils import VIEWSETS_ORDERMAP
from fabric_interface.views import RedirectHomeView
from viewsets import ModelViewSet, SLUG
from viewsets.patterns import PLACEHOLDER_PATTERN


class HostDetailView(PermissionRequiredMixin, DetailContextMixin, DetailView):
    permission_required = 'hosts.view_host'
    accept_global_perms = True


class HostCreateView(PermissionRequiredMixin, CreateContextMixin, CreateView):
    permission_required = 'hosts.add_host'
    accept_global_perms = True

    success_url = reverse_lazy('host_index')

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, _(u"Created {model} '{slug}' successfully.".format(
                model=self.model._meta.verbose_name,
                slug=self.object.slug
            ))
        )
        return reverse('host_detail', kwargs={'slug': self.object.slug})


class HostUpdateView(PermissionRequiredMixin, UpdateContextMixin, UpdateView):
    permission_required = 'hosts.change_host'
    accept_global_perms = True

    success_url = reverse_lazy('host_index')

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, _(u"Updated {model} '{slug}' successfully.".format(
                model=self.model._meta.verbose_name,
                slug=self.object.slug
            ))
        )
        return reverse('host_detail', kwargs={'slug': self.object.slug})


class HostDeleteView(PermissionRequiredMixin, DeleteContextMixin, DeleteView):
    permission_required = 'hosts.delete_host'
    accept_global_perms = True

    success_url = reverse_lazy('host_index')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        messages.add_message(
            request, messages.SUCCESS, _(u"Deleted {model} '{slug}' successfully.".format(
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
        self.views[b'list_view']['view'] = RedirectHomeView
        self.views[b'detail_view'] = {
            b'view': HostDetailView,
            b'pattern': PLACEHOLDER_PATTERN + br'/',
            b'name': b'detail',
        }
        self.views[b'update_view'] = {
            b'view': HostUpdateView,
            b'pattern': PLACEHOLDER_PATTERN + br'/update/',
            b'name': b'update',
        }
        self.views[b'delete_view'] = {
            b'view': HostDeleteView,
            b'pattern': PLACEHOLDER_PATTERN + br'/delete/',
            b'name': b'delete',
        }
        self.views[b'create_view'] = {
            b'view': HostCreateView,
            b'pattern': br'create/',
            b'name': b'create',
        }
        self.views = SortedDict(self.views)
        self.views.keyOrder = sorted(self.views.keyOrder, key=VIEWSETS_ORDERMAP.__getitem__)
        super(HostViewSet, self).__init__(*args, **kwargs)