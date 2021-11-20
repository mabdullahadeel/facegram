from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "id"]

        extra_kwargs = {
            "url": {"view_name": "api:users_api:user-detail", "lookup_field": "username"}
        }
        read_only_fields = ["id", "email"]

class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "id"]