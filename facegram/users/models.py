from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken

AUTH_PROVIDERS = {
    'facebook': 'facebook', 'google': 'google', 
    'twitter': 'twitter', 'github': "github", 
    'email': 'email'
}

class User(AbstractUser):
    """Default user for facegram."""
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def get_tokens(self):
        token = RefreshToken.for_user(self)
        return {
            settings.FG_JWT_AUTH['FG_JWT_ACCESS_KEY']: str(token.access_token),
            settings.FG_JWT_AUTH['FG_JWT_REFRESH_KEY']: str(token)
        }


    # def get_absolute_url(self):
    #     """Get url for user's detail view.

    #     Returns:
    #         str: URL for user detail.

    #     """
    #     return reverse("users:detail", kwargs={"username": self.username})
