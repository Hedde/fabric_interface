__author__ = 'heddevanderheide'

# Django specific
from django.db import models
from django.utils.translation import ugettext_lazy as _

# App specific
from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel
from fabric_interface.configurations.models import Configuration


class Project(TimeStampedModel):
    title = models.CharField(max_length=125)
    slug = AutoSlugField(populate_from='title')

    class Meta:
        permissions = (
            ('view_project', _(u"Can view project")),
        )

    def __unicode__(self):
        return self.title

    def get_configurations(self):
        try:
            return Configuration.objects.filter(project_id=self.pk, stage__isnull=True)
        except Configuration.DoesNotExist:
            return Configuration.objects.none()