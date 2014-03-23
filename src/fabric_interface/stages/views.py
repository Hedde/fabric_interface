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
from fabric_interface.mixins import (
    DetailContext, CreateContext, UpdateContext, DeleteContext
)
from fabric_interface.stages.forms import StageForm


class StageDetailView(DetailContext, DetailView):
    parent = None
    template_name = 'stages/stage_detail.html'

    def get_object(self, queryset=None):
        self.parent = super(StageDetailView, self).get_object(queryset)
        return self.parent.stage_set(manager='objects').get(slug=self.kwargs.get('role_slug'))


class StageCreateView(CreateContext, CreateView):
    form_class = StageForm
    template_name = 'stages/stage_form.html'

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


class StageUpdateView(UpdateContext, UpdateView):
    form_class = StageForm
    template_name = 'stages/stage_form.html'

    def get_object(self, queryset=None):
        self.parent = super(StageUpdateView, self).get_object(queryset)
        return self.parent.stage_set(manager='objects').get(slug=self.kwargs.get('role_slug'))

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


class StageDeleteView(DeleteContext, DeleteView):
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