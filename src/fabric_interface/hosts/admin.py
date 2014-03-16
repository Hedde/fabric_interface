__author__ = 'heddevanderheide'

# Django specific
from django.contrib import admin

# App specific
from fabric_interface.hosts.models import Host


admin.site.register(Host)
