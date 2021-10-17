from rest_framework.views import APIView
from rest_framework import status
from facegram.api_utils.api_response_utils import APIResponse
from facegram.mixins.serializer_version_mixin import SerializerVersionMixin
from .decorators import is_uuid_valid
from .models import PostComment
from .serializers.v1.serializers import PostCommentSerializerV1


class CommentAPIView(SerializerVersionMixin, APIView):
    """
        View handling the creation and update
        of comments on posts.
    """

    version_map = {
        'v1': {
                "get" : PostCommentSerializerV1,
            },
    }

    def get(self, request, format=None):
        """
            Returns a list of comments on a post.
        """
        post_id = request.GET.get('post_id', None)
        comments = PostComment.objects.filter(post__uuid=post_id)
        if comments.exists():
            version_serializer = self.get_serializer_class(method=self.get.__name__)
            serializer = version_serializer(comments, many=True)
            return APIResponse.success(data=serializer.data, status_code=status.HTTP_200_OK)
        
        return APIResponse.success(data=[])

    # def post(self, request, format=None):
    #     """
    #         Create a comment on a post.
    #     """
    #     pass
