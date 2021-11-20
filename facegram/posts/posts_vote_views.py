from typing import Union
from django.http.request import HttpRequest
from django.template import context
from rest_framework.serializers import BaseSerializer
from rest_framework.views import APIView
from rest_framework import status
from facegram.api_utils.api_response_utils import APIResponse
from facegram.mixins.serializer_version_mixin import SerializerVersionMixin
from .serializers.v1.serializers import PostVoteSerializerV1, PostCommentVoteSerializerV1
from .decorators import (
    is_user_allowed_to_vote_on_comment,
    user_is_allowed_to_vote_on_post
)
from .models import Post, PostCommentVotes, PostVotes




class PostVotesAPIView(SerializerVersionMixin, APIView):
    """
        View handling the creation and update
        of comments on posts.
    """

    version_map = {
        'v1': {
                "post" : PostVoteSerializerV1,
            },
    }


    @user_is_allowed_to_vote_on_post
    def post(self, request: HttpRequest, format=None, *args, **kwargs):
        """
            Add/Remove reaction/vote on the post
        """
        try:
            vote: PostVotes = kwargs.get('vote', None)      # set by the decorator
            if vote:                             # Update Vote
                if vote.voter != request.user:
                    return APIResponse.error(status_code=status.HTTP_401_UNAUTHORIZED, message="vote update denied")
                serializer = self.get_serializer_class(method=self.post.__name__)(vote, data=request.data, partial=True)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return APIResponse.success()
            else:                                  # Create Vote
                post = Post.objects.get(id=request.GET.get('post_id', None))
                serializer = self.get_serializer_class(method=self.post.__name__)(data=request.data, context={'request': request, 'post': post})
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return APIResponse.success()

            return APIResponse.error()
        except Exception as e:
            return APIResponse.error(message=str(e))


    @user_is_allowed_to_vote_on_post
    def delete(self, request: HttpRequest, format=None, *args, **kwargs):
        """
            Delete vote on the post
        """
        try:
            vote: PostVotes = kwargs.get('vote', None)      # set by the decorator
            if not vote or vote.voter != request.user:
                return APIResponse.error(message="action not allowed", status_code=status.HTTP_403_FORBIDDEN)
            
            vote.delete()
            return APIResponse.success()

        except Exception as e:
            return APIResponse.error(message=str(e))



class PostCommentVoteView(SerializerVersionMixin, APIView):
    """
        View handling the creation and update
        of comments on posts.
    """

    version_map = {
        'v1': {
                "post" : PostCommentVoteSerializerV1,
            },
    }

    @is_user_allowed_to_vote_on_comment
    def post(self, request: HttpRequest, format=None, *args, **kwargs):
        """
            Add/Remove reaction/vote on the comment related to as post
        """
        try:
            comment_vote: Union[PostCommentVotes, None] = kwargs.get('comment_vote', None)      # set by the decorator
            if comment_vote:                             # Update Vote
                if comment_vote.voter != request.user:
                    return APIResponse.error(status_code=status.HTTP_401_UNAUTHORIZED, message="vote update denied")

                serializer: BaseSerializer = self.get_serializer_class(method=self.post.__name__)(comment_vote, data=request.data, partial=True)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return APIResponse.success(status_code=status.HTTP_200_OK)
                else:
                    return APIResponse.error(message=serializer.errors)
            else:                                       # Create Vote
                serializer: BaseSerializer = self.get_serializer_class(method=self.post.__name__)(data=request.data, context={'request': request})
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return APIResponse.success(status_code=status.HTTP_200_OK)

            return APIResponse.error()
        except Exception as e:
            return APIResponse.error(message=str(e))