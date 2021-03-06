from facegram.users.models import User
from django.conf import settings
from facegram.utils.randoms import get_random_string
from .models import OAuthScopes

def save_state_to_db(ip, state, provider):
    """
        Save the state to db
    """
    scope = OAuthScopes.objects.create(
        scope=state,
        provider=provider,
        ip=ip,
    )
    scope.save()
    return None

def get_github_authorization_url(request, redirect_uri):
    """
        URL to redirect the client to
        in order to authorize from the github
    """
    # SOCIAL_AUTH_GITHUB_SCOPE
    github_base_url = "https://github.com/login/oauth/authorize"
    state = get_random_string(length=20)

    authorization_uri = "%s?client_id=%s&redirect_uri=%s&state=%s&response_type=%s&scope=%s" % (
        github_base_url,
        settings.SOCIAL_AUTH_GITHUB_KEY,
        redirect_uri,
        state,
        "code",
        ",".join(settings.SOCIAL_AUTH_GITHUB_SCOPE),
    )

    save_state_to_db(
        ip=request.META['REMOTE_ADDR'],
        state=state,
        provider="GH",
    )

    return authorization_uri

class UserResponse:
    
    @staticmethod
    def get_user_payload(user: User):
        return {
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "id": user.id,
            "tokens": user.get_tokens()
        }