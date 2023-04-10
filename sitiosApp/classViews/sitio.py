from django.urls import reverse_lazy
from django.views import generic

from ..models import Sitio
from ..forms import frmSitio

base_dir_url = 'pages/sitio/'
list_page = 'sitio_list'

class base():
    model = Sitio

class baseCU(base):
    form_class = frmSitio.SitioForm
    success_url = reverse_lazy(list_page)


# list
class listSitio(base, generic.ListView):
    context_object_name = 'objects'
    template_name = base_dir_url + 'list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# create
class createSitio(baseCU, generic.CreateView):
    template_name = base_dir_url + 'create.html'


# update
class updateSitio(baseCU, generic.UpdateView):
    context_object_name = 'object'
    template_name = base_dir_url + 'update.html'


# delete
class deleteSitio(base, generic.DeleteView):
    template_name = base_dir_url + 'delete.html'
    success_url = reverse_lazy(list_page)


# details
class detailsSitio(base, generic.DetailView):
    template_name = base_dir_url + 'details.html'
