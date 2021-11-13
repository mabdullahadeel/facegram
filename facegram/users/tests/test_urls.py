import pytest
from django.urls import resolve, reverse

from facegram.users.models import User

pytestmark = pytest.mark.django_db


class TestUsersUrls:
    user_app_name: str = 'users_api'
    base_url: str = "/api/auth/user/"

    def test_user_me(self):
        api_endpoint: str = self.base_url + "me/"
        path_name: str = self.user_app_name + ":user-me"

        assert reverse(path_name) == api_endpoint
        assert resolve(api_endpoint).view_name == path_name

    def test_user_detail(self, user: User):
        api_endpoint: str = self.base_url + str(user.username) + "/"
        path_name: str = self.user_app_name + ":user-detail"

        assert reverse(path_name, kwargs={"username": user.username}) == api_endpoint
        assert resolve(api_endpoint).view_name == path_name

