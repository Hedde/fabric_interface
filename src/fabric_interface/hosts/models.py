__author__ = 'heddevanderheide'

# Django specific
from django.db import models
from django.utils.translation import ugettext_lazy as _

# App specific
from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel


class Host(TimeStampedModel):
    ip = models.GenericIPAddressField(blank=True, null=True)
    alias = models.CharField(max_length=175)
    slug = AutoSlugField(populate_from='alias')
    projects = models.ManyToManyField('projects.Project', blank=True, null=True, verbose_name=_(u"Projects"))

    class Meta:
        permissions = (
            ('view_host', _(u"Can view host")),
        )

    def __unicode__(self):
        if self.alias and self.ip:
            return "{alias} ({ip})".format(**{
                'alias': self.alias,
                'ip': self.ip
            })
        return self.alias or self.ip