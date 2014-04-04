__author__ = 'heddevanderheide'

# App specific
from django_tables2 import tables, A, columns
from fabric_interface.stages.models import Stage


class StageTable(tables.Table):  # todo find out how to access the dynamic project slug before reverse is called
    role = columns.LinkColumn('project_stage_detail', kwargs={'slug': 'example-com', 'role_slug': A('slug')})

    class Meta:
        model = Stage
        template = "fabric_interface/tables/bootstrap.html"

        fields = ('role', 'created', 'modified',)