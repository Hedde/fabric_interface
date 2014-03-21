__author__ = 'heddevanderheide'

# Django specific
from django import forms

# App specific
from fabric_interface.stages.models import Stage


class StageForm(forms.ModelForm):
    class Meta:
        model = Stage
