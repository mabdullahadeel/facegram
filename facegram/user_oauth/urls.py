from django.urls import path
from facegram.user_oauth.views import GithubLogin

app_name = "user_oauth"

urlpatterns = [
    path("github/", view=GithubLogin.as_view(), name="github_login"),
]