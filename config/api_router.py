from os import name
from django.contrib.staticfiles.urls import urlpatterns
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.conf import settings

from facegram.users.urls import router as users_router

user_api_router = DefaultRouter()
user_api_router.registry.extend(users_router.registry)


urlpatterns = [
    # version-1 (v1) routers
    path(f'{settings.REST_API_V1}/users/c/', include((user_api_router.urls, 'users_api'), namespace='v1')),
    path(f'{settings.REST_API_V1}/user-profile/', include(('facegram.profiles.urls', 'user_profile_api'), namespace='v1')),
    # version-2 (v2) routers
]

# urlpatterns = [
#     path('users/c/', include((user_api_router.urls, 'users_api'), namespace='users_api')),
#     path('user-profile/', include('facegram.profiles.urls', namespace='user_profile_api')),
# ]
