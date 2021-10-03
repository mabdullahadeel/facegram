from django.urls import path, include
from . import posts_view

app_name = "posts_api"

urlpatterns = [
    path('', posts_view.PostsListView.as_view(), name='get_posts'),
    path('post/<str:uuid>/', posts_view.PostRetrieveView.as_view(), name='get_post'),
    path('create/', posts_view.PostCreateView.as_view(), name='create_post'),
    path('<str:uuid>/', posts_view.PostUpdateDelete.as_view(), name='posts_update_delete'),
]