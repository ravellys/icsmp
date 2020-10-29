import pytest
from django.urls import reverse
from model_mommy import mommy

from icsmp_project.aulas.models import Video
from icsmp_project.django_assertions import assert_contains


@pytest.fixture
def video(db):
    v = mommy.make(Video)
    return v


@pytest.fixture
def resp(client, video):
    return client.get(reverse('aulas:video', args=(video.slug, )))


def test_status_code(resp):
    assert resp.status_code == 200


def test_title_video(resp, video):
    assert_contains(resp, video.titulo)


def test_content_video(resp, video):
    assert_contains(resp, f'<iframe src="https://www.youtube.com/embed/{video.v_id}')


@pytest.fixture
def resp_not_found(client, video):
    return client.get(reverse('aulas:video', args=(video.slug+'_not_found',)))


def test_status_code_not_found(resp_not_found):
    assert resp_not_found.status_code == 404
