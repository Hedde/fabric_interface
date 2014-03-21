__author__ = 'heddevanderheide'

# Django specific
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import (
    DetailView, CreateView
)

# App specific
from fabric_interface.stages.forms import StageForm


class StageDetailView(DetailView):
    parent = None
    template_name = 'stages/stage_detail.html'

    def get_object(self, queryset=None):
        self.parent = super(StageDetailView, self).get_object(queryset)
        return self.parent.stage_set(manager='objects').get(slug=self.kwargs.get('role_slug'))


class StageCreateView(CreateView):
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
