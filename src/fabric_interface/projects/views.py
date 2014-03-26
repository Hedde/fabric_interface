__author__ = 'heddevanderheide'

# Django specific
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import (
    DetailView, CreateView, UpdateView, DeleteView
)

# App specific
from fabric_interface.mixins import (
    DetailContext, CreateContext, UpdateContext, DeleteContext
)
from fabric_interface.projects.models import Project
from fabric_interface.stages.views import (
    StageDetailView, StageCreateView, StageUpdateView, StageDeleteView
)
from fabric_interface.views import RedirectHomeView
from guardian.mixins import PermissionRequiredMixin
from viewsets import ModelViewSet, SLUG
from viewsets.patterns import PLACEHOLDER_PATTERN


class ProjectDetailView(PermissionRequiredMixin, DetailContext, DetailView):
    permission_required = 'projects.view_project'
    accept_global_perms = True

    def dispatch(self, request, *args, **kwargs):
        return super(ProjectDetailView, self).dispatch(request, *args, **kwargs)


class ProjectCreateView(PermissionRequiredMixin, CreateContext, CreateView):
    permission_required = 'projects.add_project'
    accept_global_perms = True

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, _(u"Created {model} '{slug}' succesfully.".format(
                model=self.model._meta.verbose_name,
                slug=self.object.slug
            ))
        )
        return reverse('project_detail', kwargs={'slug': self.object.slug})


class ProjectUpdateView(PermissionRequiredMixin, UpdateContext, UpdateView):
    permission_required = 'projects.edit_project'
    accept_global_perms = True

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, _(u"Updated {model} '{slug}' succesfully.".format(
                model=self.model._meta.verbose_name,
                slug=self.object.slug
            ))
        )
        return reverse('project_detail', kwargs={'slug': self.object.slug})


class ProjectDeleteView(PermissionRequiredMixin, DeleteContext, DeleteView):
    permission_required = 'projects.delete_project'
    accept_global_perms = True

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


class ProjectViewSet(ModelViewSet):
    model = Project
    id_pattern = SLUG

    def __init__(self, *args, **kwargs):
        # Project CRUD
        self.views[b'list_view']['view'] = RedirectHomeView
        self.views[b'detail_view']['view'] = ProjectDetailView
        self.views[b'create_view']['view'] = ProjectCreateView
        self.views[b'update_view']['view'] = ProjectUpdateView
        self.views[b'delete_view']['view'] = ProjectDeleteView

        # Stage CRUD
        self.views[b'stage_create_view'] = {
            b'view': StageCreateView,
            b'pattern': PLACEHOLDER_PATTERN + br'/stage/create/',
            b'name': b'stage_create',
        }
        self.views[b'stage_update_view'] = {
            b'view': StageUpdateView,
            b'pattern': PLACEHOLDER_PATTERN + br'/stage/' + br'(?P<role_slug>[\w-]+)' + br'/update/',
            b'name': b'stage_update',
        }
        self.views[b'stage_delete_view'] = {
            b'view': StageDeleteView,
            b'pattern': PLACEHOLDER_PATTERN + br'/stage/' + br'(?P<role_slug>[\w-]+)' + br'/delete/',
            b'name': b'stage_delete',
        }
        self.views[b'stage_view'] = {
            b'view': StageDetailView,
            b'pattern': PLACEHOLDER_PATTERN + br'/stage/' + br'(?P<role_slug>[\w-]+)',
            b'name': b'stage_detail',
        }

        super(ProjectViewSet, self).__init__(*args, **kwargs)