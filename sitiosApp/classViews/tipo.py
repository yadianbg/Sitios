from django.urls import reverse_lazy
from django.views import generic

from ..models import TipoSitio
from ..forms import frmTipo

base_dir_url = 'pages/tipo/'
list_page = 'tipoSitio_list'

class base():
    model = TipoSitio

class baseCU(base):
    form_class = frmTipo.TipoSitioForm
    success_url = reverse_lazy(list_page)


# list
class listTipoSitio(base, generic.ListView):
    context_object_name = 'objects'
    template_name = base_dir_url + 'list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# create
class createTipoSitio(baseCU, generic.CreateView):
    template_name = base_dir_url + 'create.html'


# update
class updateTipoSitio(baseCU, generic.UpdateView):
    context_object_name = 'object'
    template_name = base_dir_url + 'update.html'


# delete
class deleteTipoSitio(base, generic.DeleteView):
    template_name = base_dir_url + 'delete.html'
    success_url = reverse_lazy(list_page)


# details
class detailsTipoSitio(base, generic.DetailView):
    template_name = base_dir_url + 'details.html'
