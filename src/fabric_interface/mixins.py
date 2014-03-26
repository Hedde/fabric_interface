__author__ = 'heddevanderheide'

# Django specific
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _


class SuperuserOnlyMixin(object):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(SuperuserOnlyMixin, self).dispatch(request, *args, **kwargs)


class BaseContext(object):
    action = 'view'

    def get_context_data(self, **kwargs):
        context = super(BaseContext, self).get_context_data(**kwargs)
        context.update({
            'title': self.title,
            'action': self.action
        })
        return context


class DetailContext(BaseContext):
    title = _(u"View")
    action = 'view'


class UpdateContext(BaseContext):
    title = _(u"Update")
    action = 'update'


class CreateContext(BaseContext):
    title = _(u"Create")
    action = 'create'


class DeleteContext(BaseContext):
    title = _(u"Delete")
    action = 'delete'