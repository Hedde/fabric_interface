from fabric_interface.formulae.forms import FormulaForm

__author__ = 'heddevanderheide'

# Django specific
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

# App specific
from fabric_interface.formulae.models import Formula
from fabric_interface.mixins import (
    DetailContextMixin, CreateContextMixin, UpdateContextMixin, DeleteContextMixin
)
from fabric_interface.mixins import PermissionRequiredMixin
from viewsets import ModelViewSet, SLUG


class FormulaListView(PermissionRequiredMixin, ListView):
    permission_required = 'formulae.view_formula'
    accept_global_terms = True

    def get_context_data(self, **kwargs):
        context = super(FormulaListView, self).get_context_data(**kwargs)
        context['object'] = self.get_queryset()[0] if self.get_queryset() else None
        context['form'] = FormulaForm()
        return context


class FormulaDetailView(PermissionRequiredMixin, DetailContextMixin, DetailView):
    permission_required = 'formulae.view_formula'
    accept_global_perms = True

    def get_context_data(self, **kwargs):
        context = super(FormulaDetailView, self).get_context_data(**kwargs)
        context['form'] = FormulaForm(instance=self.object)
        return context


class FormulaCreateView(PermissionRequiredMixin, CreateContextMixin, CreateView):
    permission_required = 'formulae.add_formula'
    accept_global_perms = True

    form_class = FormulaForm
    template_name = 'formulae/formula_list.html'
    success_url = reverse_lazy('formula_index')

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, _(u"Created {model} '{slug}' succesfully.".format(
                model=self.model._meta.verbose_name,
                slug=self.object.slug
            ))
        )
        return reverse('formula_detail', kwargs={'slug': self.object.slug})


class FormulaUpdateView(PermissionRequiredMixin, UpdateContextMixin, UpdateView):
    permission_required = 'formulae.change_formula'
    accept_global_perms = True

    form_class = FormulaForm
    template_name = 'formulae/formula_detail.html'
    success_url = reverse_lazy('formula_index')

    def form_valid(self, form):
        return super(FormulaUpdateView, self).form_valid(form)

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, _(u"Updated {model} '{slug}' succesfully.".format(
                model=self.model._meta.verbose_name,
                slug=self.object.slug
            ))
        )
        return reverse('formula_detail', kwargs={'slug': self.object.slug})


class FormulaDeleteView(PermissionRequiredMixin, DeleteContextMixin, DeleteView):
    permission_required = 'formulae.delete_formula'
    accept_global_perms = True

    success_url = reverse_lazy('formula_index')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        messages.add_message(
            self.request, messages.SUCCESS, _(u"Deleted {model} '{slug}' succesfully.".format(
                model=self.model._meta.verbose_name,
                slug=self.object.slug
            ))
        )
        self.object.delete()
        return HttpResponseRedirect(success_url)


class FormulaViewSet(ModelViewSet):
    model = Formula
    id_pattern = SLUG

    def __init__(self, *args, **kwargs):
        self.views[b'list_view']['view'] = FormulaListView
        self.views[b'detail_view']['view'] = FormulaDetailView
        self.views[b'create_view']['view'] = FormulaCreateView
        self.views[b'update_view']['view'] = FormulaUpdateView
        self.views[b'delete_view']['view'] = FormulaDeleteView
        super(FormulaViewSet, self).__init__(*args, **kwargs)