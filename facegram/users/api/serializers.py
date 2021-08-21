from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "url"]

        extra_kwargs = {
            "url": {"view_name": "users_api:user-detail", "lookup_field": "username"}
        }
