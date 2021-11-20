from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('profile/', include('facegram.profiles.urls', namespace='user_profile_api')),
    path('posts/', include('facegram.posts.urls', namespace='posts_api')),
]
