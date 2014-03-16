__author__ = 'heddevanderheide'

# Django specific
from django.db import models

# App specific
from django_extensions.db.models import TimeStampedModel


class Stage(TimeStampedModel):
    project = models.ForeignKey('projects.Project', blank=True, null=True)
    host = models.ManyToManyField('hosts.Host', blank=True, null=True)
    role = models.CharField(max_length=125, blank=True, null=True)

    def __unicode__(self):
        return self.role