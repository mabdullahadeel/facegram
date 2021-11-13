import pytest
from rest_framework.test import APIClient
from rest_framework.response import Response
from facegram.utils.fgtesting.response import TestAPIResponse


from facegram.users.models import User
from faker import Faker

pytestmark = pytest.mark.django_db


class TestUserManagement:
    base_endpoint = '/api/auth/user/'
    user_details_url = base_endpoint + 'me/'

    def test_get_user_details_unauthenticated(self, api_client: APIClient):
        response: Response = api_client.get(self.user_details_url)
        assert response.status_code == 401

    
    def test_get_user_details_authenticated(self, user: User, authenticated_client: APIClient, test_response: TestAPIResponse):
        expected_response = {
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "id": user.id,
        }
        response: Response = authenticated_client.get(self.user_details_url)
        assert response.status_code == 200
        assert response.data == test_response.success(data=expected_response)


    def test_update_user_details_authenticated(self, user: User, authenticated_client: APIClient, test_response: TestAPIResponse):
        new_user = Faker()

        data = {
            "first_name": new_user.first_name(),
            "last_name": new_user.last_name(),
            "username": new_user.user_name(),
        }
        patch_user_url = self.base_endpoint + str(user.username) + '/'
        response: Response = authenticated_client.patch(patch_user_url, data=data)
        assert response.status_code == 200
        data["id"] = user.id
        data["email"] = user.email
        assert response.data == test_response.success(data=data)


    def test_email_update_not_allowed(self, user: User, authenticated_client: APIClient, test_response: TestAPIResponse):
        new_email = Faker().email()

        data = {
            "email": new_email
        }
        patch_user_url = self.base_endpoint + str(user.username) + '/'
        response: Response = authenticated_client.patch(patch_user_url, data=data)
        assert response.status_code == 200
        assert response.data["data"]["email"] == user.email
