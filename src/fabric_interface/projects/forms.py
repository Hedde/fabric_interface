__author__ = 'heddevanderheide'

# Django specific
from django import forms

# App specific
from fabric_interface.formulae.models import Fabfile
from fabric_interface.projects.models import Project


class ProjectForm(forms.ModelForm):
    user = None  # todo user/guardian based implementation

    class Meta:
        model = Project

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        # Only select top level structures.
        self.fields['fabfile'] = forms.ModelChoiceField(
            queryset=Fabfile.objects.filter(parent__isnull=True),
            required=False
        )