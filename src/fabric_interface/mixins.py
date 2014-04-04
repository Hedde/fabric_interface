__author__ = 'heddevanderheide'

# Django specific
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _

# App specific
from guardian.mixins import PermissionRequiredMixin
from guardian.utils import get_403_or_None


class SuperuserOnlyMixin(object):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(SuperuserOnlyMixin, self).dispatch(request, *args, **kwargs)


class PermissionRequiredMixin(PermissionRequiredMixin):
    def check_permissions(self, request):
        """
        Checks if *request.user* has all permissions returned by
        *get_required_permissions* method.

        :param request: Original request.
        """
        if hasattr(self, 'action') and self.action == 'create':
            obj = None
        else:
            obj = (hasattr(self, 'get_object') and self.get_object()
                   or getattr(self, 'object', None))

        forbidden = get_403_or_None(request,
            perms=self.get_required_permissions(request),
            obj=obj,
            login_url=self.login_url,
            redirect_field_name=self.redirect_field_name,
            return_403=self.return_403,
            accept_global_perms=self.accept_global_perms
        )
        if forbidden:
            self.on_permission_check_fail(request, forbidden, obj=obj)
        if forbidden and self.raise_exception:
            raise PermissionDenied()
        return forbidden


class BaseContextMixin(object):
    action = 'view'

    def get_context_data(self, **kwargs):
        context = super(BaseContextMixin, self).get_context_data(**kwargs)
        context.update({
            'title': self.title,
            'action': self.action
        })
        return context


class DetailContextMixin(BaseContextMixin):
    title = _(u"View")
    action = 'view'


class UpdateContextMixin(BaseContextMixin):
    title = _(u"Update")
    action = 'update'


class CreateContextMixin(BaseContextMixin):
    title = _(u"Create")
    action = 'create'


class DeleteContextMixin(BaseContextMixin):
    title = _(u"Delete")
    action = 'delete'