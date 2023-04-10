from django.urls import reverse_lazy
from django.views import generic

from ..models import Provincia
from ..forms import frmProvincia

base_dir_url = 'pages/provincia/'
list_page = 'provincia_list'

class base():
    model = Provincia

class baseCU(base):
    form_class = frmProvincia.ProvinciaForm
    success_url = reverse_lazy(list_page)


# list
class listProvincia(base, generic.ListView):
    context_object_name = 'objects'
    template_name = base_dir_url + 'list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# create
class createProvincia(baseCU, generic.CreateView):
    template_name = base_dir_url + 'create.html'


# update
class updateProvincia(baseCU, generic.UpdateView):
    context_object_name = 'object'
    template_name = base_dir_url + 'update.html'


# delete
class deleteProvincia(base, generic.DeleteView):
    template_name = base_dir_url + 'delete.html'
    success_url = reverse_lazy(list_page)


# details
class detailsProvincia(base, generic.DetailView):
    template_name = base_dir_url + 'details.html'
