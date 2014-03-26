__author__ = 'heddevanderheide'

# Django specific
from django.contrib import messages
from django.contrib.auth.views import login
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, RedirectView
from django.utils.translation import ugettext_lazy as _
from django.views.generic import (
    DetailView, CreateView, UpdateView, DeleteView
)

# App specific
from fabric_interface.decorators import add_welcome_message
from fabric_interface.forms import (
    UserForm, UserUpdateForm, UserPermissionsUpdateForm
)
from fabric_interface.mixins import (
    SuperuserOnlyMixin, BaseContext, DetailContext, CreateContext, UpdateContext, DeleteContext
)
from fabric_interface.models import User
from viewsets import ModelViewSet, PK


login = add_welcome_message(login)


class HomeView(BaseContext, TemplateView):
    template_name = 'fabric_interface/home.html'
    title = _(u"Home")


class RedirectHomeView(RedirectView):
    url = reverse_lazy('home')


class UserDetailView(SuperuserOnlyMixin, DetailContext, DetailView):
    template_name = 'fabric_interface/users/user_detail.html'


class UserCreateView(SuperuserOnlyMixin, CreateContext, CreateView):
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


class UserUpdateView(SuperuserOnlyMixin, UpdateContext, UpdateView):
    form_class = UserUpdateForm
    template_name = 'fabric_interface/users/user_form.html'

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, _(u"Updated {model} '{pk}' succesfully.".format(
                model=self.model._meta.verbose_name,
                pk=self.object.pk
            ))
        )
        return reverse('user_detail', kwargs={'pk': self.object.pk})


class UserPermissionsUpdateView(SuperuserOnlyMixin, UpdateContext, UpdateView):
    form_class = UserPermissionsUpdateForm
    template_name = 'fabric_interface/users/user_permissions_form.html'

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, _(u"Updated {model} '{pk}' succesfully.".format(
                model=self.model._meta.verbose_name,
                pk=self.object.pk
            ))
        )
        return reverse('user_detail', kwargs={'pk': self.object.pk})


class UserDeleteView(SuperuserOnlyMixin, DeleteContext, DeleteView):
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
    main_view = b'list_view'
    model = User
    views = {
        b'list_view': {
            b'view': RedirectHomeView,
            b'pattern': br'',
            b'name': b'index',
        },
        b'detail_view': {
            b'view': UserDetailView,
            b'pattern': PK,
            b'name': b'detail',
        },
        b'create_view': {
            b'view': UserCreateView,
            b'pattern': br'create/',
            b'name': b'create',
        },
        b'update_view': {
            b'view': UserUpdateView,
            b'pattern': PK + br'/update',
            b'name': b'update',
        },
        b'update_permissions_view': {
            b'view': UserPermissionsUpdateView,
            b'pattern': PK + br'/permissions',
            b'name': b'update_permissions',
        },
        b'delete_view': {
            b'view': UserDeleteView,
            b'pattern': PK + br'/delete',
            b'name': b'delete',
        },
    }