__author__ = 'heddevanderheide'

# Django specific
from django import forms

# App specific
from fabric_interface.projects.models import Project
from fabric_interface.stages.models import Stage


class StageForm(forms.ModelForm):
    queryset = None

    class Meta:
        model = Stage

    def __init__(self, *args, **kwargs):
        self.queryset = Project.objects.filter(slug=kwargs.pop('project_slug'))
        super(StageForm, self).__init__(*args, **kwargs)
        self.fields['project'] = forms.ModelChoiceField(
            queryset=self.queryset,
            initial=self.queryset.get()
        )