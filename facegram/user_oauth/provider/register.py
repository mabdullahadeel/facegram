from random import random
from typing import Tuple
from django.contrib.auth import authenticate, get_user_model, login
from rest_framework.exceptions import AuthenticationFailed
from facegram.utils.randoms import id_generator
from facegram.users.models import User
from facegram.user_oauth.utils import get_user_payload


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
                registered_user: User = login(user=user)
                
                return get_user_payload(registered_user)
            else:
                raise AuthenticationFailed(detail='Please continue your login with ' + filtering_by_email[0].auth_provider)
        else:
            username = RegisterSocialUser.generate_username(user_data.get("name"))
            first_name, last_name = RegisterSocialUser.get_names(user_data)
            user: User = get_user_model().objects.create_user(
                username=username,
                email=user_data.get("email"),
                first_name=first_name,
                last_name=last_name,
                auth_provider=provider,
            )
            user.is_verified = True
            user.save()
            t_password: str = id_generator()
            new_user: User = authenticate(email=user_data.get("email"), password=t_password)
            return get_user_payload(new_user)
