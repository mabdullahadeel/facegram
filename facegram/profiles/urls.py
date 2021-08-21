from rest_framework.routers import SimpleRouter
from django.urls import path
from . import views

app_name='user_profile_api'

router = SimpleRouter()

urlpatterns = [
    path("<str:username>", views.RetrieveUserProfileAPI.as_view(), name="my_profile_get"),
    path("u/<str:username>", views.UpdateUserProfileAPI.as_view(), name="my_profile_patch"),
]

urlpatterns += router.urls