__author__ = 'heddevanderheide'

# Django specific
from django.contrib import admin

# App specific
from fabric_interface.projects.models import Project
from fabric_interface.stages.admin import StageInline


class ProjectAdmin(admin.ModelAdmin):
    inlines = (StageInline,)


admin.site.register(Project, ProjectAdmin)