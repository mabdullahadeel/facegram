import pytest
from rest_framework.test import APIClient

from facegram.users.models import User
from facegram.users.tests.factories import AdminUserFactory, UserFactory
from facegram.utils.fgtesting.response import TestAPIResponse


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def authenticated_client(api_client, user):
    api_client.force_authenticate(user)
    return api_client


@pytest.fixture
def test_response():
    return TestAPIResponse


@pytest.fixture
def fg_admin_user() -> User:
    return AdminUserFactory()


@pytest.fixture
def fg_admin_client(client, fg_admin_user):
    client.force_login(fg_admin_user)
    return client
