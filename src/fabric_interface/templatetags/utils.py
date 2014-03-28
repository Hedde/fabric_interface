__author__ = 'heddevanderheide'

# Django specific
from django import template

register = template.Library()


@register.filter('type')
def classname(obj):
    return obj.__class__.__name__


@register.filter('prepend_class_name')
def prepend(appendix, obj, separator="_"):
    return obj.__class__.__name__.lower() + separator + appendix


@register.filter('append_class_name')
def append(prefix, obj, separator="_"):
    return prefix + separator + obj.__class__.__name__.lower()


@register.filter('contains')
def contains_permission(perms, permission):
    return bool(perms.user.user_permissions.filter(codename=permission))