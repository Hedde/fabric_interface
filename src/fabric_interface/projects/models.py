__author__ = 'heddevanderheide'

# Django specific
from django.db import models
from django.utils.translation import ugettext_lazy as _

# App specific
from django_extensions.db.models import TimeStampedModel


class Project(TimeStampedModel):
    title = models.CharField(max_length=125)
    slug = models.SlugField(unique=True)

    class Meta:
        permissions = (
            ('view_project', _(u"Can view project")),
        )

    def __unicode__(self):
        return self.title