__author__ = 'heddevanderheide'

# Django specific
from django.db import models
from django.utils.translation import ugettext_lazy as _

# App specific
from django_extensions.db.models import TimeStampedModel
from fabric_interface.projects import constants


class Configuration(TimeStampedModel):
    project = models.ForeignKey('projects.Project')
    stage = models.ForeignKey('stages.Stage', null=True, blank=True)

    key = models.CharField(max_length=255)
    value = models.CharField(max_length=500, null=True, blank=True)
    value_number = models.FloatField(verbose_name='Value', null=True, blank=True, default=0)
    value_boolean = models.BooleanField(verbose_name='Value', default=False)

    data_type = models.CharField(
        choices=constants.DATA_TYPES, null=True, blank=True, max_length=10, default=constants.TYPE_STRING
    )

    prompt = models.BooleanField(default=False, help_text=_(u"Prompt me before deploying"))
    sensitive_value = models.BooleanField(default=False, help_text=_(u"Sensitive value that should not be logged"))

    class Meta:
        permissions = (
            ('view_configuration', _(u"Can view configuration")),
        )

    def __unicode__(self):
        return '{}: {}'.format(self.key, self.value)

    def get_value(self):
        if self.data_type == constants.TYPE_BOOLEAN:
            return self.value_boolean
        elif self.data_type == constants.TYPE_NUMBER:
            return self.value_number

        return self.value

    def get_display_value(self):
        if self.sensitive_value:
            return "*****"

        return self.get_value()