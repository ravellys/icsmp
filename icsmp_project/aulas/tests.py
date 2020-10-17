import pytest
from django.test import Client
from django.urls import reverse

from icsmp_project.django_assertions import assert_contains


@pytest.fixture
def resp(client: Client):
    resp = client.get(reverse('aulas:video', args=('motivacao',)))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title_video(resp):
    assert_contains(resp, '<h1>Videos</h1>')


def test_content_video(resp):
    assert_contains(resp, '<iframe src="https://www.youtube.com/embed/')
