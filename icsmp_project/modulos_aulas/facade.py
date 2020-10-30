from icsmp_project.modulos_aulas.models import ModuloAula


def list_modulos_ordenados():
    return list(ModuloAula.objects.order_by('order').all())


def encontrar_modulo(slug):
    return ModuloAula.objects.get(slug=slug)


def listar_aulas(modulo: ModuloAula):
    return list(modulo.aula_set.order_by('order').all())
