__author__ = 'heddevanderheide'

# Django specific
from django.conf.urls import patterns, url, include
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

# App specific
from viewsets import ModelViewSet, SLUG
from fabric_interface.projects.models import Project
from fabric_interface.stages.models import Stage

urlpatterns = patterns('',
    url('^$', lambda request: HttpResponseRedirect(reverse_lazy('project_index')), name='home'),
    url('', include(ModelViewSet(Project, id_pattern=SLUG).urls)),
    # url('', include(ModelViewSet(Stage, id_pattern=SLUG).urls)),
)