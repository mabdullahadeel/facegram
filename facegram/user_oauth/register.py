import random
from typing import Tuple
from django.contrib.auth import get_user_model, login
from rest_framework.exceptions import AuthenticationFailed
from facegram.utils.randoms import id_generator
from facegram.users.models import User
from facegram.user_oauth.utils import UserResponse


class RegisterSocialUser:
    @staticmethod
    def generate_username(name: str) -> str:
        username = "".join(name.split(" ")).lower()
        if not get_user_model().objects.filter(username=username).exists():
            return username
        else:
            random_username = username + str(random.randint(0, 1000))
            return RegisterSocialUser.generate_username(random_username)
            
    @staticmethod
    def get_names(user_data: dict) -> Tuple:
        name: str = user_data.get("name")
        names: list = name.split(" ")
        return names[0], names[1]


    def register_social_user(provider: str, user_data: dict) -> str:
        filtering_by_email = get_user_model().objects.filter(email=user_data.get("email"))

        if filtering_by_email.exists():
            user: User = filtering_by_email.first()
            if provider == user.auth_provider:                
                return UserResponse.get_user_payload(user)
            else:
                raise AuthenticationFailed(detail='Please continue your login with ' + filtering_by_email[0].auth_provider)
        else:
            username = RegisterSocialUser.generate_username(user_data.get("login") or user_data.get("name"))
            first_name, last_name = RegisterSocialUser.get_names(user_data)
            t_password: str = id_generator()
            user: User = get_user_model().objects.create_user(
                username=username,
                email=user_data.get("email"),
                first_name=first_name,
                last_name=last_name,
                auth_provider=provider,
            )
            user.is_verified = True
            user.set_password(t_password)
            user.save()
            return UserResponse.get_user_payload(user)
