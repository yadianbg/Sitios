from rest_framework import serializers
from ...models import TipoSitio

# Modelo
class TipoSitioModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSitio
        fields = ['id', 'nombre']