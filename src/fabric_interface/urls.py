__author__ = 'heddevanderheide'

# Django specific
from django.conf.urls import patterns, url, include

# App specific
from fabric_interface.views import HomeView
from fabric_interface.projects.views import ProjectViewSet
from fabric_interface.hosts.views import HostViewSet


urlpatterns = patterns('',
    url('^$', HomeView.as_view(), name='home'),
    url('', include(ProjectViewSet().urls)),
    url('', include(HostViewSet().urls)),
)