from django import forms
from ..models import Provincia
# Creamos la clase para almacenar los datos del formulario
# Hacemos que extienda de forms.ModelForm
class ProvinciaForm(forms.ModelForm):
    # Añadimos la clase meta para trabajar con los atributos de ModelForm
    class Meta:
        model = Provincia # Seleccionamos el modelo al que se le estará creando el formulario
        exclude = ('id',) # Seleccionamos los campos,

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)