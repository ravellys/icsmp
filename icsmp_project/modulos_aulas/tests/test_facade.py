import pytest
from model_mommy import mommy

from icsmp_project.modulos_aulas import facade
from icsmp_project.modulos_aulas.models import ModuloAula


@pytest.fixture
def modulos(db):
    return [mommy.make(ModuloAula, nome=s) for s in ['Antes', 'Depois']]


def test_list_modulos(modulos):
    modulo_ord = list(sorted(modulos, key=lambda modulo: modulo.order))
    assert facade.list_modulos_ordenados() == modulo_ord
