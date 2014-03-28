__author__ = 'heddevanderheide'

# Django specific
from django.db import models

# App specific
from django_extensions.db.models import TimeStampedModel
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Formula(MPTTModel, TimeStampedModel):
    name = models.CharField(max_length=128)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    def __unicode__(self):
        return self.name