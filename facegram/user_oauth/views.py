from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .o_auth_utils import get_github_authorization_url


class GithubLogin(SocialLoginView, APIView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = settings.SOCIAL_AUTH_GITHUB_CALLBACK
    client_class = OAuth2Client


    def get(self, request, *args, **kwargs):
        """
            returns an authorization_uri to
            redirect the user along with the
            state to track CSRF
        """
        redirect_uri = request.GET.get('redirect_uri', None)
        if not redirect_uri or not redirect_uri in settings.SOCIAL_AUTH_ALLOWED_REDIRECT_URIS:
            return Response(data= {"error": "Invalid URI"}, status=status.HTTP_400_BAD_REQUEST)
        
        authorization_uri = get_github_authorization_url(request=request, redirect_uri=redirect_uri)
        return Response(data= {"authorization_uri": authorization_uri}, status=status.HTTP_200_OK)

