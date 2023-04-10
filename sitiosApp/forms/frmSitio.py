from django import forms
from ..models import Sitio, TipoSitio, Provincia

from crispy_forms.helper import FormHelper
from dal import autocomplete

class SitioForm(forms.ModelForm):
    class Meta:
        model = Sitio
        exclude = ('id',)

    tipo: forms.ModelChoiceField(
        queryset = TipoSitio.objects.all(),
        widget = autocomplete.ModelSelect2(url='dal_sitio', attrs={
            'data-placeholder': 'Tipo'
        })
    )

    provincia: forms.ModelChoiceField(
        queryset = Provincia.objects.all(),
        widget = autocomplete.ModelSelect2(url='dal_provincia', attrs={
            'data-placeholder': 'Provincia'
        })
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
