from dal import autocomplete
from ..models import TipoSitio, Provincia

class TipoSelec(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        return TipoSitio.objects.all()

class ProvinciaSelec(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        return Provincia.objects.all()
