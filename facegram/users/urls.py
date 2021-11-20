from rest_framework.routers import SimpleRouter
from .api.views import UserViewSet
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView, 
    TokenVerifyView
)

app_name='users_api'


urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

router = SimpleRouter()
router.register('', UserViewSet)
"""
Router Urls:
    me/ -> me ~ GET (name='user-me')
    <str:username>/ -> me ~ PATCH, GET (name='user-detail')
"""

urlpatterns += router.urls
