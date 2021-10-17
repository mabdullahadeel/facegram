from django.urls import path
from . import posts_view
from . import posts_comment_views

app_name = "posts_api"

urlpatterns = [
    # Posts Comments CRUD
    path('comments/', posts_comment_views.CommentAPIView.as_view(), name='get_comments'),
    # Posts CRUD
    path('post/<str:uuid>/', posts_view.PostRetrieveView.as_view(), name='get_post'),
    path('create/', posts_view.PostCreateView.as_view(), name='create_post'),
    path('<str:uuid>/', posts_view.PostUpdateDelete.as_view(), name='posts_update_delete'),
    path('', posts_view.PostsListView.as_view(), name='get_posts'),
]