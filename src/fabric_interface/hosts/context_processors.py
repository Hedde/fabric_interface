__author__ = 'heddevanderheide'

# Django specific
from fabric_interface.projects.models import Project
from fabric_interface.hosts.models import Host


def hosts(request):
    """
    Adds host QuerySet context variable to the context.
    """
    view_name = request.resolver_match.view_name
    kwargs = request.resolver_match.kwargs

    slug = kwargs.get('slug')

    if 'project_' in view_name and slug:
        return {
            'host_list': Host.objects.filter(projects__slug=slug)
        }

    return {'host_list': Host.objects.all()}