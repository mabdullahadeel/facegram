import pytest
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient

from facegram.posts.models import Post, PostVotes
from facegram.utils.fgtesting.response import TestAPIResponse


pytestmark = pytest.mark.django_db


class TestPostVoteViewsV1:

    base_endpoint = '/api/v1/posts/vote/'

    def test_post_upvote(self, authenticated_client: APIClient, post: Post):
        post_upvote_url = self.base_endpoint + '?post_id=' + str(post.id)
        data = {
            "reaction": "UV"
        }
        response: Response = authenticated_client.post(post_upvote_url, data=data)
        assert response.status_code == status.HTTP_200_OK
        assert PostVotes.objects.count() == 1
        assert PostVotes.objects.all().first().post.id == post.id

        assert response.data == TestAPIResponse.success()


    def test_post_downvote(self, authenticated_client: APIClient, post: Post):
        post_downvote_url = self.base_endpoint + '?post_id=' + str(post.id)
        data = {
            "reaction": "DV"
        }
        response: Response = authenticated_client.post(post_downvote_url, data=data)
        assert response.status_code == status.HTTP_200_OK
        assert PostVotes.objects.count() == 1
        assert PostVotes.objects.all().first().post.id == post.id
        
        assert response.data == TestAPIResponse.success()


    def test_delete_vote_on_post(self, authenticated_client: APIClient, post: Post):
        # Create Vote
        post_upvote_delete_url = self.base_endpoint + '?post_id=' + str(post.id)
        data = {
            "reaction": "UV"
        }
        response: Response = authenticated_client.post(post_upvote_delete_url, data=data)
        assert response.status_code == status.HTTP_200_OK

        # Delete Vote
        response: Response = authenticated_client.delete(post_upvote_delete_url)
        assert response.status_code == status.HTTP_200_OK
        assert PostVotes.objects.count() == 0
        assert response.data == TestAPIResponse.success()