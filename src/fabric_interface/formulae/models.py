__author__ = 'heddevanderheide'

# Django specific
from django.db import models
from django.utils.translation import ugettext_lazy as _

# App specific
from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


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
        return self.name


class FormulaPosition(MPTTModel, TimeStampedModel):
    family = models.CharField(max_length=128, blank=True, null=True)

    formula = models.ForeignKey('formulae.Formula')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    def __unicode__(self):
        return self.formula.name