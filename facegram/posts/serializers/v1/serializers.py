from django.db.models import fields
from rest_framework import serializers
from facegram.posts.models import Post
from facegram.users.api.serializers import UserPostSerializer


class PostSerializerV1(serializers.ModelSerializer):
    author = UserPostSerializer(read_only=True)
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ('created_at', 'updated_at', 'author', 'id')


    def create(self, validated_data):
        user = None
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            user = request.user

        validated_data['author'] = user
        return Post.objects.create(**validated_data)
