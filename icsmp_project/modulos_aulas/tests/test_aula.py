import pytest
from django.urls import reverse
from model_mommy import mommy

from icsmp_project.django_assertions import assert_contains
from icsmp_project.modulos_aulas.models import Aula


@pytest.fixture
def aula(db):
    return mommy.make(Aula)


@pytest.fixture
def resp(client, aula):
    return client.get(reverse('modulos_aulas:aula', args=(aula.slug, )))


def test_status_code(resp):
    assert resp.status_code == 200


def test_nome_aula(resp, aula):
    assert_contains(resp, aula.nome)


def test_content_video(resp, aula):
    assert_contains(resp, f'<iframe src="https://www.youtube.com/embed/{aula.v_id}')


@pytest.fixture
def resp_not_found(client, aula):
    return client.get(reverse('modulos_aulas:aula', args=(aula.slug+'_not_found',)))


def test_status_code_not_found(resp_not_found):
    assert resp_not_found.status_code == 404
