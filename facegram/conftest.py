import pytest

from facegram.users.models import User
from facegram.users.tests.factories import UserFactory
from rest_framework.test import APIClient


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()
