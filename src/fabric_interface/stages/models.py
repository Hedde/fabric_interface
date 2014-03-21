__author__ = 'heddevanderheide'

# Django specific
from django.db import models
from django.utils.translation import ugettext_lazy as _

# App specific
from django_extensions.db.models import TimeStampedModel


class Stage(TimeStampedModel):
    project = models.ForeignKey('projects.Project', blank=True, null=True)
    host = models.ManyToManyField('hosts.Host', blank=True, null=True, verbose_name=_(u"Hosts"))
    role = models.CharField(max_length=125, blank=True, null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        unique_together = (
            ('project', 'slug'),
        )

    def __unicode__(self):
        return self.role