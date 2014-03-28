__author__ = 'heddevanderheide'

# Django specific
from django.conf.urls import patterns, url, include

# App specific
from fabric_interface.formulae.views import FormulaeView


urlpatterns = patterns('',
   url('^$', FormulaeView.as_view(), name='test'),
)