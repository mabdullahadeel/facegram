from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from facegram.api_utils.api_response_utils import APIResponse
from facegram.mixins import serializer_version_mixin
from mixins.serializer_version_mixin import SerializerVersionMixin
from .serializers.v1.serializers import PostSerializerV1, PostUpdateSerializerV1
from .decorators import is_uuid_valid
from .models import Post


class PostsListView(SerializerVersionMixin, APIView):
    parser_classes = (MultiPartParser, FormParser)

    version_map = {
        'v1': {
                "get" : PostSerializerV1,
                "post" : PostSerializerV1,
                "put" : PostUpdateSerializerV1,
            },
    }

    def get(self, request, format=None):
        posts = Post.objects.all()
        if posts.exists():
            version_serializer= self.get_serializer_class(method=self.get.__name__)
            serializer = version_serializer(posts, many=True)
            return APIResponse.success(data=serializer.data, status_code=status.HTTP_200_OK)
        return APIResponse.success(data=[], message="No posts yet", status_code=status.HTTP_204_NO_CONTENT)


class PostRetrieveView(SerializerVersionMixin, APIView):

    version_map = {
        'v1': {
                "get" : PostSerializerV1,
            },
    }

    @is_uuid_valid
    def get(self, request, format=None, uuid=None):
        post = Post.objects.filter(uuid=uuid)
        if post.exists():
            version_serializer= self.get_serializer_class(method=self.get.__name__)
            serializer = version_serializer(post.first())
            return APIResponse.success(data=serializer.data, status_code=status.HTTP_200_OK)
        else:
            return APIResponse.success(data=[], message="Post not found", status_code=status.HTTP_404_NOT_FOUND)


class PostCreateView(SerializerVersionMixin, APIView):
    parser_classes = (MultiPartParser, FormParser)

    version_map = {
        'v1': {
                "get" : PostSerializerV1,
                "post" : PostSerializerV1,
            },
    }

    def post(self, request, format=None):
        if not request.data:
            return APIResponse.error(
                data=[],
                message="No data provided...")
        serializer = self.get_serializer_class(method=self.post.__name__)(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return APIResponse.success(data=serializer.data, status_code=status.HTTP_201_CREATED)
        return APIResponse.error(data=serializer.errors)




class PostUpdateDelete(SerializerVersionMixin, APIView):
    parser_classes = (MultiPartParser, FormParser)

    version_map = {
        'v1': {
                "put" : PostUpdateSerializerV1,
            },
    }

    @is_uuid_valid
    def put(self, request, format=None, uuid=None):
        request_data = request.data
        if not request_data:
            return APIResponse.error(data=[], message="No data provided...")

        post = Post.objects.filter(uuid=uuid)
        if not post.exists():
            return APIResponse.error(data=[], message="Post not found...", status_code=status.HTTP_404_NOT_FOUND)

        if post.first().author != request.user:
            return APIResponse.error(data=[], message="You are not allowed to edit this post...", status_code=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer_class(method=self.put.__name__)(post.first(), data=request_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return APIResponse.success(data=serializer.data, status_code=status.HTTP_200_OK)

        return APIResponse.error(data=serializer.errors)


    @is_uuid_valid
    def delete(self, request, format=None, uuid=None):
        post = Post.objects.filter(uuid=uuid)

        if not post.exists():
            return APIResponse.error(data=[], message="Post not found...", status_code=status.HTTP_404_NOT_FOUND)

        if post.first().author != request.user:
            return APIResponse.error(data=[], message="You are not allowed to delete this post...", status_code=status.HTTP_403_FORBIDDEN)

        post.first().delete()
        return APIResponse.success(data=[], status_code=status.HTTP_204_NO_CONTENT)