import requests
from django.conf import settings
# from facegram.user_oauth import provider
from facegram.user_oauth.register import RegisterSocialUser
from facegram.users.models import AUTH_PROVIDERS

class FGGitHubAuth:
    def __init__(self, code):
        self.code: str = code

    web_url = "https://github.com"
    api_url = "https://api.github.com"

    
    def _get_access_token(self) -> str:
        """
            Get access token from github
        """
        try:
            url = self.web_url + "/login/oauth/access_token"
            data = {
                "client_id": settings.SOCIAL_AUTH_GITHUB_KEY,
                "client_secret": settings.SOCIAL_AUTH_GITHUB_SECRET,
                "code": self.code
            }
            headers = {
                "Accept": "application/json"
            }
            response = requests.post(url, data=data, headers=headers)
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

    
    def _get_user_email(self, access_token: str) -> str:
        """
            Get user email from github
        """
        try:
            email_url = self.api_url + "/user/emails"
            headers = {
                "Authorization": f"token {access_token}"
            }
            email = None
            resp = requests.get(email_url, headers=headers, timeout=12)
            resp.raise_for_status()
            emails = resp.json()
            if resp.status_code == 200 and emails:
                email = emails[0]
                primary_emails = [
                    e for e in emails if not isinstance(e, dict) or e.get("primary")
                ]
                if primary_emails:
                    email = primary_emails[0]
                if isinstance(email, dict):
                    email = email.get("email", "")
            return email
        except Exception as e:
            raise e

    
    def login_user(self) -> dict:
        """
            Login user from github
        """
        try:
            access_token = self._get_access_token()
            user_info = self._get_user_info(access_token)
            email = self._get_user_email(access_token)
            if email:
                user_info["email"] = email
            return RegisterSocialUser.register_social_user(provider=AUTH_PROVIDERS.get("github"), user_data=user_info)
        except requests.exceptions.Timeout as e:
            raise Exception("Opps! cannot communicate to github. Please try again.")
        except requests.exceptions.RequestException as e:
            raise Exception("Opps! cannot communicate to github. Please try again.")
        except requests.exceptions.HTTPError as e:
            raise Exception("Opps! cannot communicate to github. Please try again.")
        except Exception as e:
            raise e
