from icsmp_project.modulos_artigos.models import ModuloArtigo
from icsmp_project.modulos_aulas import facade


def listar_modulos_ordenados(request):
    return {'MODULOS_AULAS': facade.list_modulos_ordenados()}


def listar_modulos_artigos_ordenados(request):
    return {'MODULOS_ARTIGOS': ModuloArtigo.objects.order_by('order').all()}
