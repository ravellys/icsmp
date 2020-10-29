import pytest
from django.test import Client
from django.urls import reverse
from model_mommy import mommy

from icsmp_project.aulas.models import Video
from icsmp_project.django_assertions import assert_contains


@pytest.fixture
def videos(db):
    v = mommy.make(Video, 3)
    return v


@pytest.fixture
def resp(client: Client, videos):
    return client.get(reverse('aulas:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


def test_lista_video(resp, videos):
    for video in videos:
        assert_contains(resp, video.titulo)


def test_link_video(resp, videos):
    for v in videos:
        video_link = reverse("aulas:video", args=(v.slug,))
        assert_contains(resp, video_link)
