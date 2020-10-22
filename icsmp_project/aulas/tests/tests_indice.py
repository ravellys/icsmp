import pytest
from django.test import Client
from django.urls import reverse

from icsmp_project.django_assertions import assert_contains


@pytest.fixture
def resp(client: Client):
    return client.get(reverse('aulas:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    "titulo",
    [
        "video 01",
        "video 02"
    ])
def test_lista_video(resp, titulo):
    assert_contains(resp, titulo)


@pytest.mark.parametrize(
    "slug",
    [
        "video-01",
        "video-02"
    ])
def test_link_video(resp, slug):
    video_link = reverse("aulas:video", args=(slug,))
    assert_contains(resp, video_link)
