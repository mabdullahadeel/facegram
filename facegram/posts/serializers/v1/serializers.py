from rest_framework import serializers
from facegram.posts.models import Post, PostComment, PostVotes, PostCommentVotes
from facegram.users.api.serializers import UserPostSerializer


class PostSerializerV1(serializers.ModelSerializer):
    author = UserPostSerializer(read_only=True)
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ('created_at', 'updated_at', 'author', 'id', 'uuid')


    def create(self, validated_data):
        user = None
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            user = request.user

        validated_data['author'] = user
        return Post.objects.create(**validated_data)


class PostUpdateSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Post
        read_only_fields = ('created_at', 'updated_at','id', 'uuid')
        exclude = ('author', 'created_at')


class PostCommentSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = "__all__"
        read_only_fields = ('created_at', 'updated_at', 'id', 'uuid', 'post', 'commenter', 'total_likes')


class PostVoteSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = PostVotes
        fields = '__all__'
        read_only_fields = ('created_at', 'last_modified', 'id', 'uuid', 'post', 'voter')


    def create(self, validated_data):
        user = None
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            user = request.user
        post = self.context.get('post')
        validated_data['post'] = post
        validated_data['voter'] = user
        return PostVotes.objects.create(**validated_data)


class PostCommentVoteSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = PostCommentVotes
        fields = ('total_likes',)
        read_only_fields = ('created_at', 'last_modified', 'id', 'post_comment', 'voter')
