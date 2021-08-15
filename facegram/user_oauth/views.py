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

    # https://github.com/login/oauth/authorize?client_id={}&redirect_uri={}&state={}&response_type=code&scope=user:email,read:user


    def get(self, request, *args, **kwargs):
        """
            returns an authorization_uri to
            redirect to the user along with the state
            to keep track of the state of the login.
        """
        redirect_uri = request.GET.get('redirect_uri', None)
        if not redirect_uri or not redirect_uri in settings.SOCIAL_AUTH_ALLOWED_REDIRECT_URIS:
            return Response(data= {"error": "Invalid URI"}, status=status.HTTP_400_BAD_REQUEST)
        
        # request.META.get("REMOTE_ADDR")
        return Response(data= {"greet": "Hello there"}, status=status.HTTP_200_OK)

