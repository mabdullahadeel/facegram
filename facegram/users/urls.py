from rest_framework.routers import SimpleRouter
from .api.views import UserViewSet
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView
)

app_name='users_api'


urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
router = SimpleRouter()
router.register('', UserViewSet)

urlpatterns += router.urls
