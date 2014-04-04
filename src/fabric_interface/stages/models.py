__author__ = 'heddevanderheide'

# Django specific
from django.db import models
from django.utils.translation import ugettext_lazy as _

# App specific
from django_extensions.db.models import TimeStampedModel
from fabric_interface.projects.models import Configuration


class Stage(TimeStampedModel):
    project = models.ForeignKey('projects.Project', blank=True, null=True)
    hosts = models.ManyToManyField('hosts.Host', blank=True, null=True, verbose_name=_(u"Hosts"))
    role = models.CharField(max_length=125, blank=True, null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        permissions = (
            ('view_stage', _(u"Can view stage")),
        )
        unique_together = (
            ('project', 'slug'),
        )

    def __unicode__(self):
        return self.role

    def get_configurations(self):
        # todo overloading
        try:
            return Configuration.objects.filter(stage__id=self.pk)
        except Configuration.DoesNotExist:
            return Configuration.objects.none()