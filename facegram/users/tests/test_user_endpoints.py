import pytest
from rest_framework.test import APIClient

from facegram.users.models import User
from factory import Faker


pytestmark = pytest.mark.django_db


class TestUserManagement:
    """
        Testing the endpoints provided by dj_rest_auth
    """

    endpoint = '/api/auth/user/'

    def test_get_user_details_unauthenticated(self, api_client: APIClient):
        response = api_client.get(self.endpoint)
        assert response.status_code == 401

    
    def test_get_user_details(self, user: User, authenticated_client: APIClient):
        expected_response = {
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "id": user.id,
        }
        response = authenticated_client.get(self.endpoint)
        assert response.status_code == 200
        assert response.data == expected_response


    # def test_update_user_details(self, user: User, authenticated_client: APIClient):
    #     new_first_name = Faker().first_name()
    #     new_last_name = Faker().last_name()
    #     new_email = Faker().email()
    #     new_username = Faker().user_name()




        


