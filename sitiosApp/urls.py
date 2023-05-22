from sitiosApp import views
from .classViews import tipo, provincia, sitio, dal
from django.urls import path, re_path

urlpatterns = [
    # Index
    path('', views.index, name='homepage'),

    # Tipo de sitio
    path('tipos/', tipo.listTipoSitio.as_view(), name='tipoSitio_list'),
    path('tipo/create', tipo.createTipoSitio.as_view(), name='tipoSitio_create'),
    re_path('tipo/update/(?P<pk>[0-9a-f]{32})', tipo.updateTipoSitio.as_view(), name='tipoSitio_update'),
    re_path('tipo/delete/(?P<pk>[0-9a-f]{32})', tipo.deleteTipoSitio.as_view(), name='tipoSitio_delete'),
    re_path('tipos/(?P<pk>[0-9a-f]{32})', tipo.detailsTipoSitio.as_view(), name='tipoSitio_details'),

    # Provincia
    path('provincias/', provincia.listProvincia.as_view(), name='provincia_list'),
    path('provincia/create', provincia.createProvincia.as_view(), name='provincia_create'),
    re_path('provincia/update/(?P<pk>[0-9a-f]{32})', provincia.updateProvincia.as_view(), name='provincia_update'),
    re_path('provincia/delete/(?P<pk>[0-9a-f]{32})', provincia.deleteProvincia.as_view(), name='provincia_delete'),
    re_path('provincias/(?P<pk>[0-9a-f]{32})', provincia.detailsProvincia.as_view(), name='provincia_details'),

    # Sitio
    path('sitios/', sitio.listSitio.as_view(), name='sitio_list'),
    path('sitio/create', sitio.createSitio.as_view(), name='sitio_create'),
    re_path('sitio/update/(?P<pk>[0-9a-f]{32})', sitio.updateSitio.as_view(), name='sitio_update'),
    re_path('sitio/delete/(?P<pk>[0-9a-f]{32})', sitio.deleteSitio.as_view(), name='sitio_delete'),
    re_path('sitios/(?P<pk>[0-9a-f]{32})', sitio.detailsSitio.as_view(), name='sitio_details'),

    # DAL
    path('dal/tipo', dal.TipoSelec.as_view(create_field='tipo'), name='dal_tipo'),
    path('dal/provincia', dal.ProvinciaSelec.as_view(create_field='provincia'), name='dal_provincia'),
]
