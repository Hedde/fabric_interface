__author__ = 'heddevanderheide'

# Django specific
from django.contrib import admin

# App specific
from fabric_interface.projects.models import Project
from fabric_interface.stages.admin import StageInline


class ProjectAdmin(admin.ModelAdmin):
    change_list_template = "admin/change_list_filter_sidebar.html"

    list_display = ('name', 'stages')
    list_filter = ('name',)

    inlines = (StageInline,)

    def stages(self, obj):
        return obj.stage_set.count()
    stages.short_description = 'Stages'


admin.site.register(Project, ProjectAdmin)