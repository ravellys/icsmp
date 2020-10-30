from django.shortcuts import render, get_object_or_404

# Create your views here.
from icsmp_project.modulos_aulas import facade
from icsmp_project.modulos_aulas.models import Aula


def detalhe(request, slug):
    modulo = facade.encontrar_modulo(slug=slug)
    aulas = facade.listar_aulas(modulo)
    return render(request, 'modulos_aulas/modulo_detalhe.html', {'modulo': modulo, 'aulas': aulas})


def aula(request, slug):
    aula = get_object_or_404(Aula.objects.select_related('modulo'), slug=slug)
    return render(request, 'modulos_aulas/aula.html', {'aula': aula})
