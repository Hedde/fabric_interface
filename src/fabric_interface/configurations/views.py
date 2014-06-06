__author__ = 'heddevanderheide'

# Django specific
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import (
    DetailView, CreateView, UpdateView, DeleteView
)

# App specific
from fabric_interface.configurations.tables import ConfigurationTable
from fabric_interface.projects.models import Project
from fabric_interface.mixins import (
    DetailContextMixin, CreateContextMixin, UpdateContextMixin, DeleteContextMixin, PermissionRequiredMixin
)
from fabric_interface.configurations.forms import ConfigurationForm


class ConfigurationDetailView(PermissionRequiredMixin, DetailContextMixin, DetailView):
    permission_required = 'configurations.view_configuration'
    accept_global_perms = True

    parent = None
    template_name = 'configurations/configuration_detail.html'

    pk_url_kwarg = None

    def get_object(self, queryset=None):
        self.parent = super(ConfigurationDetailView, self).get_object(queryset)
        # return self.parent.configuration_set(manager='objects').get(pk=self.kwargs.get('pk'))
        return self.parent.configuration_set.get(pk=self.kwargs.get('pk'))


class ConfigurationCreateView(PermissionRequiredMixin, CreateContextMixin, CreateView):
    permission_required = 'configurations.add_configuration'
    accept_global_perms = True

    form_class = ConfigurationForm
    template_name = 'configurations/configuration_form.html'

    def get_form_kwargs(self):
        form_kwargs = super(ConfigurationCreateView, self).get_form_kwargs()
        form_kwargs.update({
            'project_slug': self.kwargs.get('slug'),
            'stage_slug': self.request.GET.get('stage', None)
        })
        return form_kwargs

    def get_context_data(self, **kwargs):
        # Add the parent object to the context so we can mark the active navigation item
        context = super(ConfigurationCreateView, self).get_context_data(**kwargs)
        context['object'] = Project.objects.get(slug=self.kwargs.get('slug'))
        return context

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, _(u"Created {model} '{key}' successfully.".format(
                model=self.object._meta.verbose_name,
                key=self.object.key
            ))
        )
        return reverse('project_configuration_detail', kwargs={
            'slug': self.object.project.slug,
            'pk': self.object.pk
        })


class ConfigurationUpdateView(PermissionRequiredMixin, UpdateContextMixin, UpdateView):
    permission_required = 'configurations.change_configuration'
    accept_global_perms = True

    form_class = ConfigurationForm
    template_name = 'configurations/configuration_form.html'

    pk_url_kwarg = None

    def get_object(self, queryset=None):
        self.parent = super(ConfigurationUpdateView, self).get_object(queryset)
        # return self.parent.configuration_set(manager='objects').get(pk=self.kwargs.get('pk'))
        return self.parent.configuration_set.get(pk=self.kwargs.get('pk'))

    def get_form_kwargs(self):
        form_kwargs = super(ConfigurationUpdateView, self).get_form_kwargs()
        form_kwargs.update({
            'project_slug': self.kwargs.get('slug')
        })
        return form_kwargs

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, _(u"Updated {model} '{key}' successfully.".format(
                model=self.object._meta.verbose_name,
                key=self.object.key
            ))
        )
        return reverse('project_configuration_detail', kwargs={
            'slug': self.object.project.slug,
            'pk': self.object.pk
        })


class ConfigurationDeleteView(PermissionRequiredMixin, DeleteContextMixin, DeleteView):
    permission_required = 'configurations.delete_configuration'
    accept_global_perms = True

    form_class = ConfigurationForm
    template_name = 'configurations/configuration_confirm_delete.html'

    pk_url_kwarg = None

    def get_object(self, queryset=None):
        self.parent = super(ConfigurationDeleteView, self).get_object(queryset)
        # return self.parent.configuration_set(manager='objects').get(pk=self.kwargs.get('pk'))
        return self.parent.configuration_set.get(pk=self.kwargs.get('pk'))

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        messages.add_message(
            request, messages.SUCCESS, _(u"Deleted {model} '{key}' successfully.".format(
                model=self.object._meta.verbose_name,
                key=self.object.key
            ))
        )
        self.object.delete()

        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        return reverse('project_detail', kwargs={'slug': self.parent.slug})