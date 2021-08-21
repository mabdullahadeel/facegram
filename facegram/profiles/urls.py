from rest_framework.routers import SimpleRouter
from django.urls import path
from . import views

app_name='user_profile_api'

router = SimpleRouter()
# router.register('me', views.UserProfileAPIView)

urlpatterns = [
    path("<str:username>", views.RetrieveUserProfileAPI.as_view(), name="my_profile"),
]

urlpatterns += router.urls