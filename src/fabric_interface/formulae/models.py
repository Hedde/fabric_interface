__author__ = 'heddevanderheide'

# Django specific
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

# App specific
from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers.agile import PythonLexer


class Formula(TimeStampedModel):
    name = models.CharField(max_length=128)
    slug = AutoSlugField(populate_from='name')
    code = models.TextField()

    class Meta:
        permissions = (
            ('view_formula', _(u"Can view formula")),
        )
        verbose_name = _(u"formula")
        verbose_name_plural = _(u"formulae")

    def __unicode__(self):
        return self.name or 'formula'

    def prettified_code(self):
        return mark_safe(highlight(self.code, PythonLexer(), HtmlFormatter()))


class Fabfile(MPTTModel, TimeStampedModel):
    family = models.CharField(max_length=128, blank=True, null=True)
    formula = models.ForeignKey('formulae.Formula', blank=True, null=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class Meta:
        permissions = (
            ('view_fabfile', _(u"Can view fabfile")),
        )
        verbose_name = _(u"fabfile")
        verbose_name_plural = _(u"fabfiles")

    def __unicode__(self):
        return self.family