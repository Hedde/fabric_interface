__author__ = 'heddevanderheide'

# Django specific
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url('', include('fabric_interface.urls'))
)