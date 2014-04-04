__author__ = 'heddevanderheide'

# App specific
from django_tables2 import tables
from fabric_interface.projects.models import Configuration


class ConfigurationTable(tables.Table):
    class Meta:
        model = Configuration
        template = "fabric_interface/tables/bootstrap.html"

        fields = ('key', 'value', 'sensitive_value', 'prompt',)