from rest_framework.routers import SimpleRouter
from .api.views import UserViewSet
from django.urls import path

from facegram.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

app_name='users_api'


urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
router = SimpleRouter()
router.register('', UserViewSet)

urlpatterns += router.urls