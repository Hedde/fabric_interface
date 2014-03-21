
__author__ = 'heddevanderheide'

# Django specific
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import (
    CreateView, DeleteView, RedirectView
)

# App specific
from fabric_interface.projects.models import Project
from viewsets import ModelViewSet, SLUG


class ProjectListView(RedirectView):
    url = reverse_lazy('home')


class ProjectCreateView(CreateView):
    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, _(u"Added {model} succesfully.".format(
                model=self.model._meta.verbose_name
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
        self.views[b'list_view']['view'] = ProjectListView
        self.views[b'create_view']['view'] = ProjectCreateView
        self.views[b'delete_view']['view'] = ProjectDeleteView
        super(ProjectViewSet, self).__init__(*args, **kwargs)