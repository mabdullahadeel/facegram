from django.urls import path
from . import posts_views
from . import posts_comment_views
from . import posts_vote_views

app_name = "posts_api"

urlpatterns = [
    # Posts Comments CRUD
    path('comments/', posts_comment_views.CommentAPIView.as_view(), name='get_comments'),
    path('vote/', posts_vote_views.PostVotesAPIView.as_view(), name='post_vote'),
    # Posts CRUD
    path('post/<str:uuid>/', posts_views.PostRetrieveView.as_view(), name='get_post'),
    path('create/', posts_views.PostCreateView.as_view(), name='create_post'),
    path('<str:uuid>/', posts_views.PostUpdateDelete.as_view(), name='posts_update_delete'),
    path('', posts_views.PostsListView.as_view(), name='get_posts'),
]