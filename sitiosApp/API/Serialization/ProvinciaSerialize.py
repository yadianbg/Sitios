from rest_framework import serializers
from ...models import Provincia

# Modelo
class ProvinciaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = ['id', 'codigo', 'nombre']