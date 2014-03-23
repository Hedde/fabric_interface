__author__ = 'heddevanderheide'

from functools import wraps

# Django specific
from django.contrib import messages
from django.contrib.auth.views import login
from django.views.generic import TemplateView
from django.utils.decorators import available_attrs
from django.utils.translation import ugettext_lazy as _


class HomeView(TemplateView):
    template_name = 'fabric_interface/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
            'title': _(u"Home"),
            'action': 'view'
        })
        return context


def add_welcome_message(view_func):
    """
    Decorator that adds a welcome message to a response that
    succesfully authenticated.
    """
    @wraps(view_func, assigned=available_attrs(view_func))
    def _wrapped_view_func(request, *args, **kwargs):
        response = view_func(request, *args, **kwargs)
        if request.user.is_authenticated():
            messages.add_message(
                request, messages.SUCCESS, _(u"Welcome {user}!".format(
                    user=request.user.first_name or request.user.email
                ))
            )
        return response
    return _wrapped_view_func


login = add_welcome_message(login)