from django.conf.urls import url
from .views import VistaInicio, VistaListaTemas

urlpatterns = {
    url(r'^$', VistaInicio.as_view(), name="Inicio"),
    url(r'listadoTemas/', VistaListaTemas.as_view(), name="ListadoTemas"),
}