__author__ = 'heddevanderheide'

# Django specific
from django.contrib import messages
from django.contrib.auth.views import login
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _
from django.views.generic import (
    DetailView, CreateView, UpdateView, DeleteView
)

# App specific
from fabric_interface.decorators import add_welcome_message
from fabric_interface.forms import (
    UserForm, UserUpdateForm
)
from fabric_interface.mixins import (
    StaffOnlyMixin, BaseContext, DetailContext, CreateContext, UpdateContext, DeleteContext
)
from fabric_interface.models import User
from viewsets import ModelViewSet, PK


login = add_welcome_message(login)


class HomeView(BaseContext, TemplateView):
    template_name = 'fabric_interface/home.html'
    title = _(u"Home")


class UserDetailView(StaffOnlyMixin, DetailContext, DetailView):
    template_name = 'fabric_interface/users/user_detail.html'


class UserCreateView(StaffOnlyMixin, CreateContext, CreateView):
    form_class = UserForm
    success_url = reverse_lazy('home')
    template_name = 'fabric_interface/users/user_form.html'

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, _(u"Created {model} '{pk}' succesfully.".format(
                model=self.model._meta.verbose_name,
                pk=self.object.pk
            ))
        )
        return reverse('user_detail',  kwargs={'pk': self.object.pk})


class UserUpdateView(StaffOnlyMixin, UpdateContext, UpdateView):
    form_class = UserUpdateForm
    success_url = reverse_lazy('home')
    template_name = 'fabric_interface/users/user_form.html'

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, _(u"Updated {model} '{pk}' succesfully.".format(
                model=self.model._meta.verbose_name,
                pk=self.object.pk
            ))
        )
        return reverse('user_detail', kwargs={'pk': self.object.pk})


class UserDeleteView(StaffOnlyMixin, DeleteContext, DeleteView):
    success_url = reverse_lazy('home')
    template_name = 'fabric_interface/users/user_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        messages.add_message(
            self.request, messages.SUCCESS, _(u"Deleted {model} '{pk}' succesfully.".format(
                model=self.model._meta.verbose_name,
                pk=self.object.pk
            ))
        )
        self.object.delete()
        return HttpResponseRedirect(success_url)


class UserViewSet(ModelViewSet):
    model = User
    id_pattern = PK

    def __init__(self, *args, **kwargs):
        self.views[b'detail_view']['view'] = UserDetailView
        self.views[b'create_view']['view'] = UserCreateView
        self.views[b'update_view']['view'] = UserUpdateView
        self.views[b'delete_view']['view'] = UserDeleteView
        super(UserViewSet, self).__init__(*args, **kwargs)