__author__ = 'heddevanderheide'

# Django specific
from django.conf import settings

# App specific
from fabric_interface.models import User


def language(request):
    from django.utils import translation

    context_extras = {}
    context_extras['LANGUAGE'] = dict(settings.LANGUAGES).get(translation.get_language())

    return context_extras


def users(request):
    if request.user.is_authenticated() and request.user.is_superuser:
        return {
            'user_list': User.objects.exclude(id=settings.ANONYMOUS_USER_ID).exclude(id=request.user.id)
        }
    return {}


def demo(request):
    return {
        'DEMO': getattr(settings, 'FABRIC_INTERFACE_DEMO', True)
    }


def footer(request):
    """
    Adds configurable footer to the base template.
    """
    return {
        'custom_footer': getattr(settings, 'FABRIC_INTERFACE_FOOTER_TEMPLATE', None),
        'show_credits': getattr(settings, 'FABRIC_INTERFACE_SHOW_CREDITS', True)
    }