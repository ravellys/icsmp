from icsmp_project.modulos_aulas import facade


def listar_modulos_ordenados(request):
    return {'MODULOS': facade.list_modulos_ordenados()}
