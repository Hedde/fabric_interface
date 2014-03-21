__author__ = 'heddevanderheide'

# Django specific
from django import template

register = template.Library()


@register.filter('type')
def classname(obj):
    return obj.__class__.__name__
