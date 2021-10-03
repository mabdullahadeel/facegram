from os import name
from django.contrib.staticfiles.urls import urlpatterns
from django.urls import path, include
from django.conf import settings

app_name = 'api'

urlpatterns = [
    path('users/c/', include('facegram.users.urls', namespace='users_api')),
    path('profile/', include('facegram.profiles.urls', namespace='user_profile_api')),
    path('posts/', include('facegram.posts.urls', namespace='posts_api')),
]
