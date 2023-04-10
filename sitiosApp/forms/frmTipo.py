from django import forms
from ..models import TipoSitio
# Creamos la clase para almacenar los datos del formulario
# Hacemos que extienda de forms.ModelForm
class TipoSitioForm(forms.ModelForm):
    # Añadimos la clase meta para trabajar con los atributos de ModelForm
    class Meta:
        model = TipoSitio # Seleccionamos el modelo al que se le estará creando el formulario
        fields = ('nombre',) # Seleccionamos los campos,
        # fields = '__all__' # Usamos este si queremos añadir todos los campos

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)