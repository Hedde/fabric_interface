__author__ = 'heddevanderheide'

# Django specific
from fabric_interface.hosts.models import Host


def hosts(request):
    """
    Adds host QuerySet context variable to the context.

    """
    return {'host_list': Host.objects.all()}