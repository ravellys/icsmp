import pytest
from django.test import Client
from django.urls import reverse

from icsmp_project.django_assertions import assert_contains


@pytest.fixture
def resp(client: Client, db):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>ICSMP - Home</title>')


def test_title_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">')
