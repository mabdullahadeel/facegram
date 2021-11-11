import pytest
from django.urls import resolve, reverse

from facegram.users.models import User

pytestmark = pytest.mark.django_db


# Version-1 Urls
def test_user_detail(user: User):
    assert (
        reverse("api:users_api:user-detail", kwargs={"username": user.username})
        == f"/api/v1/users/c/{user.username}/"
    )
    assert resolve(f"/api/v1/users/c/{user.username}/").view_name == "api:users_api:user-detail"


def test_user_list():
    assert reverse("api:users_api:user-list") == "/api/v1/users/c"
    assert resolve("/api/v1/users/c").view_name == "api:users_api:user-list"


# def test_user_me():
#     assert reverse("users_api:user-me") == "/api/v1/users/me/"
#     assert resolve("/api/v1/users/me/").view_name == "users_api:user-me"
