__author__ = 'heddevanderheide'

# Django specific
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import (
    CreateView, DeleteView, RedirectView, UpdateView
)

# App specific
from fabric_interface.projects.models import Project
from fabric_interface.stages.views import (
    StageCreateView, StageDetailView
)
from viewsets import ModelViewSet, SLUG
from viewsets.patterns import PLACEHOLDER_PATTERN


class ProjectListView(RedirectView):
    url = reverse_lazy('home')


class ProjectCreateView(CreateView):
    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, _(u"Created {model} '{slug}' succesfully.".format(
                model=self.model._meta.verbose_name,
                slug=self.object.slug
            ))
        )
        return reverse('project_detail', kwargs={'slug': self.object.slug})


class ProjectUpdateView(UpdateView):
    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, _(u"Updated {model} '{slug}' succesfully.".format(
                model=self.model._meta.verbose_name,
                slug=self.object.slug
            ))
        )
        return reverse('project_detail', kwargs={'slug': self.object.slug})


class ProjectDeleteView(DeleteView):
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
        self.views[b'list_view']['view'] = ProjectListView
        self.views[b'create_view']['view'] = ProjectCreateView
        self.views[b'delete_view']['view'] = ProjectDeleteView
        self.views[b'update_view']['view'] = ProjectUpdateView

        # Stage CRUD
        self.views[b'stage_create_view'] = {
            b'view': StageCreateView,
            b'pattern': PLACEHOLDER_PATTERN + br'/stage/create/',
            b'name': b'stage_create',
        }
        self.views[b'stage_view'] = {
            b'view': StageDetailView,
            b'pattern': PLACEHOLDER_PATTERN + br'/stage/' + br'(?P<role_slug>[\w-]+)',
            b'name': b'stage_detail',
        }

        super(ProjectViewSet, self).__init__(*args, **kwargs)