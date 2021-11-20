from django.test.client import encode_multipart
import factory
from faker.proxy import Faker
import pytest
from typing import List, TypedDict, Optional
from rest_framework.response import Response
from rest_framework.test import APIClient
from rest_framework import status
from facegram.users.models import User
from facegram.posts.models import Post
from django.forms.models import model_to_dict
from .helpers.posts_worker import PostFactoryWorker


pytestmark = pytest.mark.django_db

class SerializedUser(TypedDict):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str

class PostsDictType(TypedDict):
    id: int
    author: Optional[SerializedUser]
    title: str
    body: str
    image: str
    privacy: str
    uuid: str
    created_at: str
    last_modified: str


class TestPostV1:
    base_endpoint = '/api/v1/posts/'


    def test_create_post(self, authenticated_client: APIClient, user: User, post: Post):
        create_post_url = self.base_endpoint + 'create/'
        PRIVACY_CHOICES = ["OM", "OF", "EO"]
        response: Response = authenticated_client.post(create_post_url, data=model_to_dict(post), format='multipart')

        author: SerializedUser = response.data["data"].pop('author')
        new_post: PostsDictType = response.data["data"]

        assert response.status_code == status.HTTP_201_CREATED
        assert Post.objects.all().count() == 2

        assert new_post["title"] == post.title
        assert new_post["body"] == post.body
        assert new_post["privacy"] in PRIVACY_CHOICES

        assert author["username"] == user.username
        assert author["email"] == user.email


    def test_get_all_posts(self, authenticated_client: APIClient, user: User):
        # Create Posts
        posts: List[PostsDictType] = PostFactoryWorker.create_test_posts(number_of_posts=5)

        # Get all posts
        response: Response = authenticated_client.get(self.base_endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["data"]) == 5
        assert Post.objects.all().count() == len(posts)


    def test_get_one_post(self, authenticated_client: APIClient, user: User):
        # Create Posts
        posts: List[PostsDictType] = PostFactoryWorker.create_test_posts(number_of_posts=5)

        # Get one post
        post_uuid = str(posts[0].uuid)
        post_id: str = posts[0].id
        get_post_url = self.base_endpoint + "post/" + post_uuid + "/"
        response: Response = authenticated_client.get(get_post_url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["data"]["uuid"] == post_uuid
        assert response.data["data"]["id"] == post_id


    def test_update_post(self, authenticated_client: APIClient):
        create_post_url = self.base_endpoint + 'create/'
        post: Post = PostFactoryWorker.create_test_post()
        response: Response = authenticated_client.post(create_post_url, data=model_to_dict(post), format='multipart')

        post_uuid: str = response.data["data"]["uuid"]

        update_post_url = self.base_endpoint + post_uuid + '/'
        updated_post: Post = PostFactoryWorker.create_test_post()
        response: Response = authenticated_client.put(update_post_url, data=model_to_dict(updated_post), format='multipart')

        assert response.status_code == status.HTTP_200_OK


    def test_delete_post(self, authenticated_client: APIClient):
        create_post_url = self.base_endpoint + 'create/'
        post: Post = PostFactoryWorker.create_test_post()
        response: Response = authenticated_client.post(create_post_url, data=model_to_dict(post), format='multipart')

        post_uuid: str = response.data["data"]["uuid"]

        delete_post_url = self.base_endpoint + post_uuid + '/'
        response: Response = authenticated_client.delete(delete_post_url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
