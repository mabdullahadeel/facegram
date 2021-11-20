import pytest
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient

from facegram.users.models import User
from facegram.posts.models import Post
from facegram.utils.fgtesting.response import TestAPIResponse
from faker import Faker

pytestmark = pytest.mark.django_db


class TestPostCommentViewV1:
    base_endpoint = '/api/v1/posts/comments/'

    def test_user_can_comment_on_post(self, authenticated_client: APIClient, public_post: Post):
        data = {
            "body": Faker().text(),
        }
        post_comment_url = self.base_endpoint + "?post_id=" + str(public_post.id)
        response: Response = authenticated_client.post(post_comment_url, data=data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['data']["post"] == public_post.id
        assert response.data['data']["body"] == data['body']


    def test_update_comment_on_post(self, api_client: APIClient, public_post: Post, user: User):
        api_client.force_authenticate(user=user)
        # create comment on post
        data = {
            "body": Faker().text(),
        }
        post_comment_url = self.base_endpoint + "?post_id=" + str(public_post.id)
        response: Response = api_client.post(post_comment_url, data=data, format='json')

        comment_id = response.data['data']['id']

        # update comment
        post_update_url = self.base_endpoint + "?comment_id=" + str(comment_id) 
        updated_data = {
            "body": Faker().text(),
        }
        response: Response = api_client.patch(post_update_url, data=updated_data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['data']["post"] == public_post.id
        assert response.data['data']["body"] == updated_data['body']


    def test_delete_comment_on_post(self, api_client: APIClient, public_post: Post, user: User):
        api_client.force_authenticate(user=user)
        # create comment on post
        data = {
            "body": Faker().text(),
        }
        post_comment_url = self.base_endpoint + "?post_id=" + str(public_post.id)
        response: Response = api_client.post(post_comment_url, data=data, format='json')

        comment_id = response.data['data']['id']
        comment_delete_url = self.base_endpoint + "?comment_id=" + str(comment_id) 

        # delete comment
        response: Response = api_client.delete(comment_delete_url, format='json')
        assert response.status_code == status.HTTP_204_NO_CONTENT


    def test_get_comments_on_post(self, api_client: APIClient, user: User, public_post: Post):
        api_client.force_authenticate(user=user)
        # create comment on post
        data = {
            "body": Faker().text(),
        }
        post_url = self.base_endpoint + "?post_id=" + str(public_post.id)
        for _ in range(5):
            response: Response = api_client.post(post_url, data=data, format='json')
            assert response.status_code == status.HTTP_201_CREATED

        # get comments
        response: Response = api_client.get(post_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['data']) == 5
        