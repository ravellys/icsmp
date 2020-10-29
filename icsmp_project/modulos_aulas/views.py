from django.shortcuts import render

# Create your views here.
from icsmp_project.modulos_aulas import facade


def detalhe(request, slug):
    modulo = facade.encontrar_modulo(slug=slug)
    return render(request, 'modulos_aulas/modulo_detalhe.html', {'modulo': modulo})
