from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Tema, TemaEjemplo

class VistaInicio(TemplateView):
    def get(self,request, **kwargs):
        return render(request, 'index.html', context=None)

class VistaListaTemas(TemplateView):
    def get(self, request, **kwargs):
        temaEjemplo = TemaEjemplo()
        return render(request, 'listadoTemas.html', {'temas': temaEjemplo.obtenerTemas()})
# Create your views here.
