from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status
from mixins.serializer_version_mixin import SerializerVersionMixin
from .serializers.v1.serializers import PostSerializerV1
from .models import Post

class PostList(SerializerVersionMixin, APIView):

    version_map = {
        'v1': {
                "get" :PostSerializerV1
            },
    }


    def get(self, request, format=None):
        posts = Post.objects.all()
        if posts.exists():
            version_serializer= self.get_serializer_class(method=self.get.__name__)
            serializer = version_serializer(posts, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data={"message": "No posts"}, status=status.HTTP_204_NO_CONTENT)
