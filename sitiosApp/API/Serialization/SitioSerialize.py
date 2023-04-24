from rest_framework import serializers
from ...models import Sitio

# Modelo
class SitioModelSerializer(serializers.ModelSerializer):
    tipo = serializers.StringRelatedField(many=False)
    provincia = serializers.StringRelatedField(many=False)

    class Meta:
        model = Sitio
        fields = ['id', 'nombre', 'direccion', 'capacidad', 'fechaApertura', 'disponible', 'foto', 'tipo', 'provincia']