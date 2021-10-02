from django.db.models import fields
from rest_framework import serializers
from facegram.posts.models import Post
from facegram.users.api.serializers import UserPostSerializer


class PostSerializerV1(serializers.ModelSerializer):
    author = UserPostSerializer(read_only=True)
    class Meta:
        model = Post
        fields = "__all__"