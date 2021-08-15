from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class GithubLogin(SocialLoginView, APIView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = settings.SOCIAL_AUTH_GITHUB_CALLBACK
    client_class = OAuth2Client


    def get(self, request, *args, **kwargs):
        """
            This method returns an authorization url to
            redirect to the user along with the state
            to keep track of the state of the login.
        """
        return Response(data= {"greet": "Hello there"}, status=status.HTTP_200_OK)

