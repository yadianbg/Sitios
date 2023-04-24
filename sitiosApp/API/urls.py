from .Controllers import TipoSitioController, ProvinciaController, SitioController
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tipoSitioApiV', TipoSitioController.TipoSitioView, basename='tipoSitioApiV')
router.register(r'tipoSitioApiMV', TipoSitioController.TipoSitioModelView, basename='tipoSitioApiMV')
router.register(r'provinciaApiV', ProvinciaController.ProvinciaView, basename='provinciaApiV')
router.register(r'provinciaApiMV', ProvinciaController.ProvinciaModelView, basename='provinciaApiMV')
router.register(r'sitioApiV', SitioController.SitioView, basename='sitioApiV')
router.register(r'sitioApiMV', SitioController.SitioModelView, basename='sitioApiMV')

urlpatterns = [
    # Tipo de sitio
    path('tipo/', TipoSitioController.TipoSitioList.as_view(), name='api_tipoSitio_list'),
    re_path('tipo/(?P<pk>[0-9a-f]{32})', TipoSitioController.TipoSitioDetails.as_view(), name='api_tipoSitio_details'),
    path('tipoApi/', TipoSitioController.TipoSitioAPI.as_view(), name='apiV_tipoSitio_list'),
    re_path('tipoApi/(?P<pk>[0-9a-f]{32})', TipoSitioController.TipoSitioAPID.as_view(), name='apiV_tipoSitio_details'),

    # Provincia
    path('provincia/', ProvinciaController.ProvinciaList.as_view(), name='api_provincia_list'),
    re_path('provincia/(?P<pk>[0-9a-f]{32})', ProvinciaController.ProvinciaDetails.as_view(), name='api_provincia_details'),
    path('provinciaApi/', ProvinciaController.ProvinciaAPI.as_view(), name='apiV_provincia_list'),
    re_path('provinciaApi/(?P<pk>[0-9a-f]{32})', ProvinciaController.ProvinciaAPID.as_view(), name='apiV_provincia_details'),

    # Sitio
    path('sitio/', SitioController.SitioList.as_view(), name='api_sitio_list'),
    re_path('sitio/(?P<pk>[0-9a-f]{32})', SitioController.SitioDetails.as_view(), name='api_sitio_details'),
    path('sitioApi/', SitioController.SitioAPI.as_view(), name='apiV_sitio_list'),
    re_path('sitioApi/(?P<pk>[0-9a-f]{32})', SitioController.SitioAPID.as_view(), name='apiV_sitio_details'),

    # GENERIC Urls
    path('', include(router.urls))
]
