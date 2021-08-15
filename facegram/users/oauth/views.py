from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.conf import settings



class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = settings.SOCIAL_AUTH_GITHUB_CALLBACK
    client_class = OAuth2Client
