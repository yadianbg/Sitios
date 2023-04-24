from .Controllers import TipoSitioController
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tipoSitioApiV', TipoSitioController.TipoSitioView, basename='tipoSitioApiV')
router.register(r'tipoSitioApiVM', TipoSitioController.TipoSitioModelView, basename='tipoSitioApiVM')

urlpatterns = [
    # Tipo Sitio
    path('tipo/', TipoSitioController.TipoSitioList.as_view(), name='api_tipoSitio_list'),
    re_path('tipo/(?P<pk>[0-9a-f]{32})', TipoSitioController.TipoSitioDetails.as_view(), name='api_tipoSitio_details'),
    path('tipoApi/', TipoSitioController.TipoSitioAPI.as_view(), name='apiV_tipoSitio_list'),
    re_path('tipoApi/(?P<pk>[0-9a-f]{32})', TipoSitioController.TipoSitioAPID.as_view(), name='apiV_tipoSitio_details'),

    # GENERIC Urls
    path('', include(router.urls))
]
