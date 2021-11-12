import requests
from django.conf import settings
# from facegram.user_oauth import provider
from facegram.user_oauth.register import RegisterSocialUser
from facegram.users.models import AUTH_PROVIDERS

class FGGitHubAuth:
    def __init__(self, code):
        self.code = code

    web_url = "https://github.com"
    api_url = "https://api.github.com"

    
    def _get_access_token(self, code: str) -> str:
        """
            Get access token from github
        """
        try:
            url = self.web_url + "/login/oauth/access_token"
            data = {
                "client_id": settings.SOCIAL_AUTH_GITHUB_KEY,
                "client_secret": settings.SOCIAL_AUTH_GITHUB_SECRET,
                "code": code
            }
            response = requests.post(url, data=data)
            return response.json()["access_token"]
        except Exception as e:
            raise e


    def _get_user_info(self, access_token: str) -> dict:
        """
            Get user info from github
        """
        try:
            url = self.api_url + "/user"
            headers = {
                "Authorization": f"token {access_token}"
            }
            response = requests.get(url, headers=headers)
            return response.json()
        except Exception as e:
            raise e

    
    def login_user(self) -> dict:
        """
            Login user from github
        """
        try:
            access_token = self._get_access_token(self.code)
            user_info = self._get_user_info(access_token)
            return RegisterSocialUser.register_social_user(provider=AUTH_PROVIDERS.get("github"), user_data=user_info)
        except Exception as e:
            raise e
