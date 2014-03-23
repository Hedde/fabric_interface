__author__ = 'heddevanderheide'

# Django specific
from django import forms

# App specific
from fabric_interface.models import User


class UserForm(forms.ModelForm):
    class Meta:
        fields = ('email', 'password')
        model = User