import pytest
from django.urls import reverse
from model_mommy import mommy

from icsmp_project.django_assertions import assert_contains
from icsmp_project.modulos_aulas.models import ModuloAula


@pytest.fixture
def modulos(db):
    return mommy.make(ModuloAula, 3)

@pytest.fixture
def resp(client, modulos):
    return client.get(reverse('base:home'))


def test_titulo_modulo(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.nome)


def test_titulo_link_modulo(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.get_absolute_url())
