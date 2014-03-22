__author__ = 'heddevanderheide'

# Django specific
from django import template

register = template.Library()


@register.filter(name='pass')
def contents(value):
    return value