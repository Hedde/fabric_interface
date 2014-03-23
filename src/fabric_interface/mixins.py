__author__ = 'heddevanderheide'

# Django specific
from django.utils.translation import ugettext_lazy as _


class DetailContext(object):
    title = _(u"View")
    action = 'view'

    def get_context_data(self, **kwargs):
        context = super(DetailContext, self).get_context_data(**kwargs)
        context.update({
            'title': self.title,
            'action': self.action
        })
        return context


class UpdateContext(DetailContext):
    title = _(u"Update")
    action = 'update'


class CreateContext(DetailContext):
    title = _(u"Create")
    action = 'create'


class DeleteContext(DetailContext):
    title = _(u"Delete")
    action = 'delete'