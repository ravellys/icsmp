import pytest
from django.test import Client
from django.urls import reverse

from icsmp_project.django_assertions import assert_contains


@pytest.fixture
def resp(client: Client):
    return client.get(reverse('aulas:video', args=('video-01',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_title_video(resp):
    assert_contains(resp, 'video')


def test_content_video(resp):
    assert_contains(resp, '<iframe src="https://www.youtube.com/embed/')
