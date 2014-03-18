__author__ = 'heddevanderheide'

# Django specific
from django.core.urlresolvers import reverse
from django.db import models

# App specific
from django_extensions.db.models import TimeStampedModel


class Project(TimeStampedModel):
    title = models.CharField(max_length=125)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.title