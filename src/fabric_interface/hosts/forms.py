__author__ = 'heddevanderheide'

# Django specific
from django import forms

# App specific
from fabric_interface.hosts.models import Host


class HostForm(forms.ModelForm):
    class Meta:
        model = Host