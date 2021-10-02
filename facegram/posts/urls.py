from django.urls import path, include
from . import views

app_name = "posts_api"

urlpatterns = [
    path('', views.PostList.as_view(), name='get_posts'),
]