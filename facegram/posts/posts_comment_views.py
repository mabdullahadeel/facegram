from django.http.request import HttpRequest
from rest_framework.serializers import BaseSerializer
from rest_framework.views import APIView
from rest_framework import status
from facegram.api_utils.api_response_utils import APIResponse
from facegram.mixins.serializer_version_mixin import SerializerVersionMixin
from .models import PostComment, Post
from .serializers.v1.serializers import PostCommentSerializerV1
from .decorators import (
    user_is_allowed_to_mutate_comment, 
    user_is_allowed_to_create_comment
)




class CommentAPIView(SerializerVersionMixin, APIView):
    """
        View handling the creation and update
        of comments on posts.
    """

    version_map = {
        'v1': {
                "get" : PostCommentSerializerV1,
                "post" : PostCommentSerializerV1,
                "patch" : PostCommentSerializerV1,
            },
    }

    def get(self, request: HttpRequest, format=None):
        """
            Returns a list of comments on a post.
            :param : post_id
        """
        try:
            post_id = request.GET.get('post_id', None)
            if not post_id:
                return APIResponse.error(data=[], message='post_id is required')

            Post.objects.get(id=post_id)
            comments = PostComment.objects.filter(post__id=post_id)
            if comments.exists():
                serializer: BaseSerializer = self.get_serializer_class(method=self.get.__name__)(comments, many=True)
                return APIResponse.success(data=serializer.data)
            return APIResponse.success(data=[])
        except Exception as e:
            if type(e) == ValueError or type(e) == Post.DoesNotExist:
                return APIResponse.error(data=[],  message=str(e))
        
        return APIResponse.error(data=[], message='Something went wrong')


    @user_is_allowed_to_create_comment
    def post(self, request: HttpRequest, format=None, *args, **kwargs):
        """
            Create a comment on a post.
        """
        try:
            commenting_post: Post = kwargs.get('post', None)      # set by the decorator
            serializer: BaseSerializer = self.get_serializer_class(method=self.post.__name__)(data=request.data, context={'request': request, 'post': commenting_post})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return APIResponse.success(data=serializer.data, status_code=status.HTTP_201_CREATED)
        except Exception as e:
            if type(e) == ValueError or type(e) == Post.DoesNotExist:
                return APIResponse.error(message=str(e))

        return APIResponse.error(message='Something went wrong')


    @user_is_allowed_to_mutate_comment
    def patch(self, request, format=None, *args, **kwargs):
        """
            Update a comment on a post.
        """
        try:
            comment = kwargs.get('comment', None)      # set by the decorator

            if comment.commenter != request.user:
                return APIResponse.error(data=[], message='comment update not allowed', status_code=status.HTTP_403_FORBIDDEN)
            
            serializer = self.get_serializer_class(method=self.patch.__name__)(comment, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return APIResponse.success(data=serializer.data, status_code=status.HTTP_200_OK)
        except Exception as e:
            return APIResponse.error(data=[], message=str(e))


    
    @user_is_allowed_to_mutate_comment
    def delete(self, request, format=None, *args, **kwargs):
        """
            Delete a comment on a post.
        """
        try:
            comment = kwargs.get('comment', None)      # set by the decorator

            if comment.commenter != request.user:
                return APIResponse.error(data=[], message='comment deletion not allowed', status_code=status.HTTP_403_FORBIDDEN)
            
            comment.delete()
            return APIResponse.success(data=[], status_code=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return APIResponse.error(data=[], message=str(e))

