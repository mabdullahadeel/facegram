from rest_framework.generics import RetrieveAPIView
from .models import Profile
from rest_framework.permissions import AllowAny
from .serializers.v1.serializers import RetrieveUserProfileSerializerV1
from facegram.mixins.serializer_version_mixin import SerializerVersionMixin


class RetrieveUserProfileAPI(SerializerVersionMixin, RetrieveAPIView):
    """
        Open API endpoint to see UserProfile details
        NOTE: No need to specify serializer_class as taken
            care of in the mixin class.
    """
    version_map = {
        'v1': RetrieveUserProfileSerializerV1,
    }
    permission_classes = [AllowAny]
    lookup_field = 'user__username'
    lookup_url_kwarg = 'username'

    def get_queryset(self):
        username = self.request.user.username
        return Profile.objects.filter(user__username=username)