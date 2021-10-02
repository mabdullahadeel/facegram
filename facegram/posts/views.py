from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
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
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data={"message": "No posts"}, status=status.HTTP_204_NO_CONTENT)


    def post(self, request, format=None):

        if not request.data:
            return Response(
                data={"message": "No data was sent with the request..."},
                status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer_class(method=self.post.__name__)(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
