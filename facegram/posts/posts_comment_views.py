from rest_framework.views import APIView
from rest_framework import serializers, status
from facegram.api_utils.api_response_utils import APIResponse
from facegram.mixins.serializer_version_mixin import SerializerVersionMixin
from .models import PostComment, Post
from .serializers.v1.serializers import PostCommentSerializerV1
from .decorators import user_is_allowed_to_comment




class CommentAPIView(SerializerVersionMixin, APIView):
    """
        View handling the creation and update
        of comments on posts.
    """

    version_map = {
        'v1': {
                "get" : PostCommentSerializerV1,
                "post" : PostCommentSerializerV1,
            },
    }

    def get(self, request, format=None):
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
                serializer = self.get_serializer_class(method=self.get.__name__)(comments, many=True)
                return APIResponse.success(data=serializer.data)

            return APIResponse.success(data=[])
        except Exception as e:
            if type(e) == ValueError or type(e) == Post.DoesNotExist:
                return APIResponse.error(data=[],  message=str(e))
        
        return APIResponse.error(data=[], message='Something went wrong')


    @user_is_allowed_to_comment
    def post(self, request, format=None, *args, **kwargs):
        """
            Create a comment on a post.
        """
        try:
            commenting_post = kwargs.get('post', None)      # set by the decorator
            request.data['post'] = commenting_post.id
            request.data['commenter'] = request.user.id
            serializer = self.get_serializer_class(method=self.post.__name__)(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return APIResponse.success(data=serializer.data, status_code=status.HTTP_201_CREATED)

        except Exception as e:
            if type(e) == ValueError or type(e) == Post.DoesNotExist:
                return APIResponse.error(data=[],  message=str(e))

        return APIResponse.error(data=[], message='Something went wrong')


    @user_is_allowed_to_comment
    def patch(self, request, format=None, *args, **kwargs):
        """
            Update a comment on a post.
        """
        try:
            post_id = request.GET.get('post_id', None)
            comment_id = request.data.get('comment_id', None)

            if not post_id or not comment_id:
                return APIResponse.error(data=[], message='post_id and comment_id are required')
            
            commenting_post = Post.objects.get(id=post_id)
            
        except Exception as e:
            return APIResponse.error(data=[], message=str(e))

