__author__ = 'heddevanderheide'


# Django specific
from django.db import models

# App specific
from django_extensions.db.models import TimeStampedModel


class Project(TimeStampedModel):
    title = models.CharField(max_length=125, blank=True, null=True)
    slug = models.SlugField()

    def __unicode__(self):
        return self.title