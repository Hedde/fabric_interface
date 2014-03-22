__author__ = 'heddevanderheide'

# Django specific
from django.conf import settings


def footer(request):
    """
    Adds configurable footer to the base template.
    """
    return {
        'custom_footer': getattr(settings, 'FABRIC_INTERFACE_FOOTER_TEMPLATE', None),
        'show_credits': getattr(settings, 'FABRIC_INTERFACE_SHOW_CREDITS', True)
    }