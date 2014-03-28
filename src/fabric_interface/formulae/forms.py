__author__ = 'heddevanderheide'

# Django specific
from django import forms

# App specific
from fabric_interface.formulae.models import FormulaPosition


class FormulaPositionForm(forms.ModelForm):
    class Meta:
        model = FormulaPosition