from django.urls import path

from facegram.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

from facegram.users.oauth.views import (
    GithubLogin
)

app_name = "users"
urlpatterns = [
    path("github/", view=GithubLogin.as_view(), name="github_login"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
