from rest_framework.routers import SimpleRouter
from .api.views import UserViewSet

app_name='users_api'

router = SimpleRouter()
router.register('', UserViewSet)

urlpatterns = router.urls