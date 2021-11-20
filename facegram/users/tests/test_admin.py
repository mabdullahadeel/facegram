import pytest
from django.urls import reverse
from django.test import Client
from django.http import HttpResponse
from facegram.users.models import User

pytestmark = pytest.mark.django_db


class TestUserAdmin:
    def test_changelist(self, fg_admin_client: Client):
        url = reverse("admin:users_user_changelist")
        response: HttpResponse = fg_admin_client.get(url)
        assert response.status_code == 200

    def test_search(self, fg_admin_client: Client):
        url = reverse("admin:users_user_changelist")
        response: HttpResponse = fg_admin_client.get(url, data={"q": "test"})
        assert response.status_code == 200

    def test_add(self, fg_admin_client: Client):
        url = reverse("admin:users_user_add")
        response: HttpResponse = fg_admin_client.get(url)
        assert response.status_code == 200

        response: HttpResponse = fg_admin_client.post(
            url,
            data={
                "username": "test",
                "password1": "My_R@ndom-P@ssw0rd",
                "password2": "My_R@ndom-P@ssw0rd",
            },
        )
        assert response.status_code == 302
        assert User.objects.filter(username="test").exists()

    def test_view_user(self, fg_admin_client: Client, fg_admin_user: User):
        user: User = User.objects.get(username=fg_admin_user.username)
        url = reverse("admin:users_user_change", kwargs={"object_id": user.pk})
        response: HttpResponse = fg_admin_client.get(url)
        assert response.status_code == 200
