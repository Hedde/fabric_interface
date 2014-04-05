from django.core.exceptions import ObjectDoesNotExist

__author__ = 'heddevanderheide'

# Django specific
from django import forms

# App specific
from fabric_interface.projects.models import Project, Configuration
from fabric_interface.stages.models import Stage


class ConfigurationForm(forms.ModelForm):
    project_queryset = None
    stage_queryset = None

    class Meta:
        model = Configuration

    def __init__(self, *args, **kwargs):
        self.project_queryset = Project.objects.filter(slug=kwargs.pop('project_slug', None))
        self.stage_queryset = Stage.objects.filter(slug=kwargs.pop('stage_slug', None))

        super(ConfigurationForm, self).__init__(*args, **kwargs)

        self.fields['project'] = forms.ModelChoiceField(
            queryset=self.project_queryset,
            initial=self.project_queryset.get()
        )

        try:
            self.fields['stage'] = forms.ModelChoiceField(
                queryset=self.stage_queryset,
                initial=self.stage_queryset.get()
            )
        except ObjectDoesNotExist:
            pass