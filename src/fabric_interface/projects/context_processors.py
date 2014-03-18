__author__ = 'heddevanderheide'

# Django specific
from fabric_interface.projects.models import Project


def projects(request):
    """
    Adds project QuerySet context variable to the context.

    """
    return {'project_list': Project.objects.all()}