from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from facegram.api_utils.api_response_utils import APIResponse
from mixins.serializer_version_mixin import SerializerVersionMixin
from .serializers.v1.serializers import PostSerializerV1
from .models import Post


class PostList(SerializerVersionMixin, APIView):

    parser_classes = (MultiPartParser, FormParser)

    version_map = {
        'v1': {
                "get" :PostSerializerV1,
                "post" :PostSerializerV1
            },
    }


    def get(self, request, format=None):
        posts = Post.objects.all()
        if posts.exists():
            version_serializer= self.get_serializer_class(method=self.get.__name__)
            serializer = version_serializer(posts, many=True)
            return APIResponse.success(data=serializer.data, status_code=status.HTTP_200_OK)

        return APIResponse.success(data=[], message="No posts yet", status_code=status.HTTP_204_NO_CONTENT)


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


    def put(self, request, format=None):
        request_data = request.data
        if not request_data:
            return APIResponse.error(data=[], message="No data provided...")

        


    def delete(self, request, format=None):
        return Response(data={"message": "DELETE method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

