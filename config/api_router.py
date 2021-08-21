from os import name
from django.contrib.staticfiles.urls import urlpatterns
from rest_framework.routers import DefaultRouter
from facegram.users.urls import router as users_router
from django.urls import path, include
from django.conf import settings

user_api_router = DefaultRouter()
user_api_router.registry.extend(users_router.registry)

urlpatterns = [
    path(f'{settings.REST_API_V1}/users/c/', include((user_api_router.urls, 'users_api'), namespace='v1')),
]
