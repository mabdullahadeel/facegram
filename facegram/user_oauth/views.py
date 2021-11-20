from django.conf import settings
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from facegram.api_utils.api_response_utils import APIResponse
from facegram.user_oauth.provider.github.github import FGGitHubAuth

from .models import OAuthScopes
from .utils import get_github_authorization_url


class GithubLogin(APIView):
    permission_classes = (AllowAny,)


    def get(self, request, *args, **kwargs):
        """
            returns an authorization_uri to
            redirect the user along with the
            state to track CSRF
        """
        redirect_uri = request.GET.get('redirect_uri', None)
        if not redirect_uri or not redirect_uri in settings.SOCIAL_AUTH_ALLOWED_REDIRECT_URIS:
            return APIResponse.error(data= {"error": "Invalid URI"})
        
        authorization_uri = get_github_authorization_url(request=request, redirect_uri=redirect_uri)
        return APIResponse.success(data= {"authorization_uri": authorization_uri})

    
    def post(self, request, *args, **kwargs):
        try:
            state = request.data.get('state', None)
            if not state:
                return APIResponse.error(data= {"error": "Invalid State"})
            
            matching_state = OAuthScopes.objects.filter(scope=state)
            if not matching_state:
                return APIResponse.error(data= {"error": "Invalid State"}, status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

            oauth_scopes = matching_state[0]
            if oauth_scopes.ip != request.META.get('REMOTE_ADDR'):
                return APIResponse.error(data= {"error": "Invalid IP"}, status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
            else:
                oauth_scopes.delete()
            
            return APIResponse.success(
                data=FGGitHubAuth(code=request.data.get('code', None)).login_user(), 
                status_code=status.HTTP_201_CREATED
                )
        except Exception as e:
            return APIResponse.error(
                data={"error": str(e)}, 
                )
