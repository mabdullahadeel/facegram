from os import name
from django.contrib.staticfiles.urls import urlpatterns
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.conf import settings

app_name = 'api'

urlpatterns = [
    path('users/c/', include('facegram.users.urls', namespace='users_api')),
    path('user-profile/', include('facegram.profiles.urls', namespace='user_profile_api')),
]


# urlpatterns = [
#     path('users/c/', include((user_api_router.urls, 'users_api'), namespace='users_api')),
#     path('user-profile/', include('facegram.profiles.urls', namespace='user_profile_api')),
# ]
