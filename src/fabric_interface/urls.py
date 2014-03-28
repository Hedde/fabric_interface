__author__ = 'heddevanderheide'

# Django specific
from django.conf.urls import patterns, url, include

# App specific
from fabric_interface.views import HomeView, login
from fabric_interface.projects.views import ProjectViewSet
from fabric_interface.hosts.views import HostViewSet
from fabric_interface.views import UserViewSet


urlpatterns = patterns('',
    url('^$', HomeView.as_view(), name='home'),
    url(r'^login/$', login, {
        'template_name': 'fabric_interface/login.html'
    }, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {
        'next_page': 'login'
    }, name='logout'),
    url('', include(ProjectViewSet().urls)),
    url('', include(HostViewSet().urls)),
    url('', include(UserViewSet().urls)),
)