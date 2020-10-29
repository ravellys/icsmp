import pytest
from django.urls import reverse
from model_mommy import mommy

from icsmp_project.django_assertions import assert_contains
from icsmp_project.modulos_aulas.models import ModuloAula


@pytest.fixture
def modulo(db):
    return mommy.make(ModuloAula)

@pytest.fixture
def resp(client, modulo):
    return client.get(reverse('modulos_aulas:detalhe', kwargs={'slug': modulo.slug}))


def test_titulo_modulo(resp, modulo):
    assert_contains(resp, modulo.nome)


def test_descricao_modulo(resp, modulo):
    assert_contains(resp, modulo.descricao)
