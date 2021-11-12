from rest_framework.routers import SimpleRouter
from .api.views import UserViewSet
from django.urls import path

app_name='users_api'


urlpatterns = []
router = SimpleRouter()
router.register('', UserViewSet)

urlpatterns += router.urls
