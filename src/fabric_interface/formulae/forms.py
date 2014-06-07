__author__ = 'heddevanderheide'

# Django specific
from django import forms
from django.utils.translation import ugettext_lazy as _

# App specific
from codemirror.widgets import CodeMirrorTextarea
from fabric_interface.formulae.models import (
    Formula, Fabfile
)


class FormulaForm(forms.ModelForm):
    code = forms.CharField(
        widget=CodeMirrorTextarea(mode="python", theme="cobalt", config={'fixedGutter': True, 'indentUnit': 4}),
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


class FabfileForm(forms.ModelForm):
    obj = None

    class Meta:
        model = Fabfile

    def __init__(self, *args, **kwargs):
        super(FabfileForm, self).__init__(*args, **kwargs)

        self.obj = kwargs.get('instance')

        if self.obj and not self.obj.parent:
            self.fields.pop('parent')

    def clean_parent(self):
        cd = self.cleaned_data['parent']

        if self.obj and self.obj == cd:
            raise forms.ValidationError(_(u"A child's parent cannot point to the child instance."))

        return cd