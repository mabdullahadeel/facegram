from rest_framework.generics import RetrieveUpdateAPIView
from .models import Profile
from .serializers.v1.serializers import ProfileSerializerV1
from facegram.mixins.serializer_version_mixin import SerializerVersionMixin


class UserProfileAPIView(SerializerVersionMixin, RetrieveUpdateAPIView):
    """
        API endpoint that allows user prifiles to be viewed or edited.
        NOTE: No need to specify serializer_class as taken
            care of in the mixin class.
    """
    version_map = {
        'v1': ProfileSerializerV1,
    }
    lookup_field = 'user__username'
    lookup_url_kwarg = 'username'

    def get_queryset(self):
        username = self.request.user.username
        return Profile.objects.filter(user__username=username)