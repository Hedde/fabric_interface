__author__ = 'heddevanderheide'

# Django specific
from django.db import models

# App specific
from django_extensions.db.models import TimeStampedModel


class Host(TimeStampedModel):
    ip = models.GenericIPAddressField(blank=True, null=True)
    alias = models.CharField(max_length=175, blank=True, null=True)

    def __unicode__(self):
        if self.alias and self.ip:
            return "{alias} ({ip})".format(**{
                'alias': self.alias,
                'ip': self.ip
            })
        return self.alias or self.ip