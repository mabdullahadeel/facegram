from django.urls import path, include
from . import views

app_name = "posts_api"

urlpatterns = [
    path('', views.PostsListView.as_view(), name='get_posts'),
    path('post/<str:uuid>/', views.PostRetrieveView.as_view(), name='get_post'),
    path('create/', views.PostCreateView.as_view(), name='create_post'),
    path('<str:uuid>/', views.PostUpdateDelete.as_view(), name='posts_update_delete'),
]