__author__ = 'heddevanderheide'

# Django specific
from django.utils.translation import ugettext_lazy as _


TYPE_BOOLEAN = 'BOOLEAN'
TYPE_NUMBER = 'NUMBER'
TYPE_STRING = 'STRING'

DATA_TYPES = (
    (TYPE_BOOLEAN, _(u"Boolean")),
    (TYPE_NUMBER, _(u"Number")),
    (TYPE_STRING, _(u"String")),
)