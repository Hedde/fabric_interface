__author__ = 'heddevanderheide'

import django_tables2 as tables

# Django specific
from django.utils.translation import ugettext_lazy as _

# App specific
from fabric_interface.projects.models import Configuration
from django.core import urlresolvers
from django.utils.html import mark_safe
from django_tables2.utils import AttributeDict


class ConfigurationActionsColumn(tables.Column):
    """
    This column allows you to pass in a list of links that will form an Action Column
    """
    empty_values = ()
    links = None
    delimiter = None

    def __init__(self, links=None, delimiter=' | ', **kwargs):
        super(ConfigurationActionsColumn, self).__init__(**kwargs)
        self.orderable = False
        self.delimiter = delimiter
        if links is not None:
            self.links = links

    def render(self, value, record, bound_column):
        if not self.links:
            raise NotImplementedError('Links not assigned.')
        if not isinstance(self.links, (list, tuple,dict)):
            raise NotImplementedError('Links must be an iterable.')

        links = []

        for link in self.links:
            title = link['title']
            url = link['url']
            attrs = link['attrs'] if 'attrs' in link else None

            attrs = AttributeDict(attrs if attrs is not None else self.attrs.get('a', {}))

            try:
                attrs['href'] = urlresolvers.reverse(url, kwargs={'slug': record.project.slug, 'pk': record.pk})
            except urlresolvers.NoReverseMatch:
                attrs['href'] = url

            links.append('<a {attrs}>{text}</a>'.format(
                attrs=attrs.as_html(),
                text=mark_safe(title)
            ))

        return mark_safe(self.delimiter.join(links))


class ConfigurationTable(tables.Table):
    actions = ConfigurationActionsColumn([
        {'title': '<i class="glyphicon glyphicon-file"></i>', 'url': 'project_configuration_detail', 'args': [tables.A('pk')],
         'attrs':{'data-toggle': 'tooltip', 'title': 'View configuration', 'data-delay': '{ "show": 300, "hide": 0 }'}},
        {'title': '<i class="glyphicon glyphicon-pencil"></i>', 'url': 'project_configuration_update', 'args': [tables.A('pk')],
         'attrs':{'data-toggle': 'tooltip', 'title': 'Edit configuration', 'data-delay': '{ "show": 300, "hide": 0 }'}},
        {'title': '<i class="glyphicon glyphicon-trash"></i>', 'url': 'project_configuration_delete', 'args': [tables.A('pk')],
         'attrs':{'data-toggle': 'tooltip', 'title': 'Delete configuration', 'data-delay': '{ "show": 300, "hide": 0 }'}},
    ], delimiter='&#160;&#160;&#160;', verbose_name=_(u"ACTIONS"))

    class Meta:
        model = Configuration
        template = "fabric_interface/tables/bootstrap.html"

        fields = ('key', 'value', 'sensitive_value', 'prompt',)

        # sequence = fields = ('first_name', 'last_name', 'is_active', 'email', 'user_level', )
        # attrs = {'class': 'table table-striped table-bordered table-hover'}