from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from facegram.profiles.models import Profile


class ProfileSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ('user',"followers","following")
        read_only_fields = ('id', 'follower_count', 'following_count', "up_votes", "down_votes")