from os import name
from django.contrib.staticfiles.urls import urlpatterns
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.conf import settings

from facegram.users.urls import router as users_router

user_api_router = DefaultRouter()
user_api_router.registry.extend(users_router.registry)

urlpatterns = [
    path('/users/c/', include((user_api_router.urls, 'users_api'), namespace='users_api')),
    path('/user-profile/', include('facegram.profiles.urls', namespace='user_profile_api')),
]
