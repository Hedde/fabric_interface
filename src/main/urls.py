__author__ = 'heddevanderheide'

# Django specific
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url('', include('fabric_interface.urls'))
)