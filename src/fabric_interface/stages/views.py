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
from fabric_interface.projects.models import Project
from fabric_interface.projects.tables import ConfigurationTable
from fabric_interface.mixins import (
    DetailContextMixin, CreateContextMixin, UpdateContextMixin, DeleteContextMixin, PermissionRequiredMixin
)
from fabric_interface.stages.forms import StageForm


class StageDetailView(PermissionRequiredMixin, DetailContextMixin, DetailView):
    permission_required = 'stages.view_stage'
    accept_global_perms = True

    parent = None
    template_name = 'stages/stage_detail.html'

    def get_context_data(self, **kwargs):
        context = super(StageDetailView, self).get_context_data(**kwargs)

        configurations = self.object.get_configurations()
        context['configurations'] = ConfigurationTable(configurations) if configurations else None

        return context

    def get_object(self, queryset=None):
        self.parent = super(StageDetailView, self).get_object(queryset)
        return self.parent.stage_set(manager='objects').get(slug=self.kwargs.get('role_slug'))


class StageCreateView(PermissionRequiredMixin, CreateContextMixin, CreateView):
    permission_required = 'stages.add_stage'
    accept_global_perms = True

    form_class = StageForm
    template_name = 'stages/stage_form.html'

    def get_form_kwargs(self):
        form_kwargs = super(StageCreateView, self).get_form_kwargs()
        form_kwargs.update({
            'project_slug': self.kwargs.get('slug')
        })
        return form_kwargs

    def get_context_data(self, **kwargs):
        # Add the parent object to the context so we can mark the active navigation item
        context = super(StageCreateView, self).get_context_data(**kwargs)
        context['object'] = Project.objects.get(slug=self.kwargs.get('slug'))
        return context

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, _(u"Created {model} '{slug}' succesfully.".format(
                model=self.object._meta.verbose_name,
                slug=self.object.role
            ))
        )
        return reverse('project_stage_detail', kwargs={
            'slug': self.object.project.slug,
            'role_slug': self.object.slug
        })


class StageUpdateView(PermissionRequiredMixin, UpdateContextMixin, UpdateView):
    permission_required = 'stages.change_stage'
    accept_global_perms = True

    form_class = StageForm
    template_name = 'stages/stage_form.html'

    def get_object(self, queryset=None):
        self.parent = super(StageUpdateView, self).get_object(queryset)
        return self.parent.stage_set(manager='objects').get(slug=self.kwargs.get('role_slug'))

    def get_form_kwargs(self):
        form_kwargs = super(StageUpdateView, self).get_form_kwargs()
        form_kwargs.update({
            'project_slug': self.kwargs.get('slug')
        })
        return form_kwargs

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, _(u"Updated {model} '{slug}' succesfully.".format(
                model=self.object._meta.verbose_name,
                slug=self.object.role
            ))
        )
        return reverse('project_stage_detail', kwargs={
            'slug': self.object.project.slug,
            'role_slug': self.object.slug
        })


class StageDeleteView(PermissionRequiredMixin, DeleteContextMixin, DeleteView):
    permission_required = 'stages.delete_stage'
    accept_global_perms = True

    form_class = StageForm
    template_name = 'stages/stage_confirm_delete.html'

    def get_object(self, queryset=None):
        self.parent = super(StageDeleteView, self).get_object(queryset)
        return self.parent.stage_set(manager='objects').get(slug=self.kwargs.get('role_slug'))

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        messages.add_message(
            self.request, messages.SUCCESS, _(u"Deleted {model} '{slug}' succesfully.".format(
                model=self.object._meta.verbose_name,
                slug=self.object.slug
            ))
        )
        self.object.delete()

        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        return reverse('project_detail', kwargs={'slug': self.parent.slug})