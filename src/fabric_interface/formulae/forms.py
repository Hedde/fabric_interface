__author__ = 'heddevanderheide'

# Django specific
from django import forms

# App specific
from codemirror.widgets import CodeMirrorTextarea
from fabric_interface.formulae.models import (
    Formula, FormulaPosition
)


class FormulaForm(forms.ModelForm):
    code = forms.CharField(
        widget=CodeMirrorTextarea(mode="python", theme="cobalt", config={'fixedGutter': True}),
        required=False
    )

    class Meta:
        model = Formula

    def clean_code(self):
        code = self.cleaned_data['code']
        try:
            eval(compile(code, 'validate', 'exec'))
        except Exception, e:
            raise forms.ValidationError(e)
        return code


class FormulaPositionForm(forms.ModelForm):
    class Meta:
        model = FormulaPosition