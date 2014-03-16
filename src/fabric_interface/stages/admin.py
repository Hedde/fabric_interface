__author__ = 'heddevanderheide'

# Django specific
from django.contrib import admin

# App specific
from fabric_interface.stages.models import Stage


class StageInline(admin.StackedInline):
    model = Stage
    extra = 0

    filter_horizontal = ('host',)