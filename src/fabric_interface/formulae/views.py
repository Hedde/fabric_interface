__author__ = 'heddevanderheide'

# Django specific
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.utils.datastructures import SortedDict
from django.utils.translation import ugettext_lazy as _
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

# App specific
from fabric_interface.formulae.forms import FormulaForm, FabfileForm
from fabric_interface.formulae.models import Formula, Fabfile
from fabric_interface.mixins import (
    PermissionRequiredMixin, DetailContextMixin, CreateContextMixin, UpdateContextMixin, DeleteContextMixin
)
from fabric_interface.utils import VIEWSETS_ORDERMAP
from viewsets import ModelViewSet, SLUG, PK
from viewsets.patterns import PLACEHOLDER_PATTERN


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# models.Formula                                                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
            self.request, messages.SUCCESS, _(u"Created {model} '{slug}' successfully.".format(
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
            self.request, messages.SUCCESS, _(u"Updated {model} '{slug}' successfully.".format(
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
            request, messages.SUCCESS, _(u"Deleted {model} '{slug}' successfully.".format(
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
        self.views[b'list_view'] = {
            b'view': FormulaListView,
            b'pattern': br'',
            b'name': b'index',
        }
        self.views[b'detail_view'] = {
            b'view': FormulaDetailView,
            b'pattern': PLACEHOLDER_PATTERN + br'/',
            b'name': b'detail',
        }
        self.views[b'update_view'] = {
            b'view': FormulaUpdateView,
            b'pattern': PLACEHOLDER_PATTERN + br'/update/',
            b'name': b'update',
        }
        self.views[b'delete_view'] = {
            b'view': FormulaDeleteView,
            b'pattern': PLACEHOLDER_PATTERN + br'/delete/',
            b'name': b'delete',
        }
        self.views[b'create_view'] = {
            b'view': FormulaCreateView,
            b'pattern': br'create/',
            b'name': b'create',
        }
        self.views = SortedDict(self.views)
        self.views.keyOrder = sorted(self.views.keyOrder, key=VIEWSETS_ORDERMAP.__getitem__)
        super(FormulaViewSet, self).__init__(*args, **kwargs)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# models.Fabfile                                                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class FabfileListView(PermissionRequiredMixin, ListView):
    permission_required = 'formulae.view_fabfile'
    accept_global_terms = True

    def get_context_data(self, **kwargs):
        context = super(FabfileListView, self).get_context_data(**kwargs)
        context['object'] = self.get_queryset()[0] if self.get_queryset() else None
        context['form'] = FabfileForm()
        return context


class FabfileDetailView(PermissionRequiredMixin, DetailContextMixin, DetailView):
    permission_required = 'formulae.view_fabfile'
    accept_global_perms = True

    def get_context_data(self, **kwargs):
        context = super(FabfileDetailView, self).get_context_data(**kwargs)
        context['form'] = Fabfile(instance=self.object)
        return context


class FabfileCreateView(PermissionRequiredMixin, CreateContextMixin, CreateView):
    permission_required = 'formulae.add_fabfile'
    accept_global_perms = True

    form_class = FabfileForm
    template_name = 'formulae/fabfile_list.html'
    success_url = reverse_lazy('fabfile_index')

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, _(u"Created {model} '{pk}' successfully.".format(
                model=self.model._meta.verbose_name,
                pk=self.object.pk
            ))
        )
        return reverse('fabfile_detail', kwargs={'pk': self.object.pk})


class FabfileUpdateView(PermissionRequiredMixin, UpdateContextMixin, UpdateView):
    permission_required = 'formulae.change_fabfile'
    accept_global_perms = True

    form_class = FabfileForm
    template_name = 'formulae/fabfile_detail.html'
    success_url = reverse_lazy('fabfile_index')

    def form_valid(self, form):
        return super(FabfileUpdateView, self).form_valid(form)

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, _(u"Updated {model} '{pk}' successfully.".format(
                model=self.model._meta.verbose_name,
                pk=self.object.pk
            ))
        )
        return reverse('fabfile_detail', kwargs={'pk': self.object.pk})


class FabfileDeleteView(PermissionRequiredMixin, DeleteContextMixin, DeleteView):
    permission_required = 'formulae.delete_fabfile'
    accept_global_perms = True

    success_url = reverse_lazy('fabfile_index')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        messages.add_message(
            request, messages.SUCCESS, _(u"Deleted {model} '{pk}' successfully.".format(
                model=self.model._meta.verbose_name,
                pk=self.object.pk
            ))
        )
        self.object.delete()
        return HttpResponseRedirect(success_url)


class FabfileViewSet(ModelViewSet):
    model = Fabfile
    id_pattern = PK

    def __init__(self, *args, **kwargs):
        self.views[b'list_view'] = {
            b'view': FabfileListView,
            b'pattern': br'',
            b'name': b'index',
        }
        self.views[b'detail_view'] = {
            b'view': FabfileDetailView,
            b'pattern': PLACEHOLDER_PATTERN + br'/',
            b'name': b'detail',
        }
        self.views[b'update_view'] = {
            b'view': FabfileUpdateView,
            b'pattern': PLACEHOLDER_PATTERN + br'/update/',
            b'name': b'update',
        }
        self.views[b'delete_view'] = {
            b'view': FabfileDeleteView,
            b'pattern': PLACEHOLDER_PATTERN + br'/delete/',
            b'name': b'delete',
        }
        self.views[b'create_view'] = {
            b'view': FabfileCreateView,
            b'pattern': br'create/',
            b'name': b'create',
        }
        self.views = SortedDict(self.views)
        self.views.keyOrder = sorted(self.views.keyOrder, key=VIEWSETS_ORDERMAP.__getitem__)
        super(FabfileViewSet, self).__init__(*args, **kwargs)