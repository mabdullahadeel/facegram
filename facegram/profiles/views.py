from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from .models import Profile
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers.v1.serializers import (
    RetrieveUserProfileSerializerV1,
    UpdateProfileSerializerV1,
    )
from facegram.mixins.serializer_version_mixin import SerializerVersionMixin
from rest_framework import status
from rest_framework.response import Response


class RetrieveUserProfileAPI(SerializerVersionMixin, RetrieveAPIView):
    """
        Open API endpoint to see UserProfile details
        NOTE: No need to specify serializer_class as taken
            care of in the mixin class.
        support ~> [GET]
    """
    version_map = {
        'v1': RetrieveUserProfileSerializerV1,
    }
    permission_classes = [AllowAny,]
    lookup_field = 'user__username'
    lookup_url_kwarg = 'username'

    def get_queryset(self):
        username = self.kwargs.get(self.lookup_url_kwarg)
        print(username)
        return Profile.objects.filter(user__username=username)


class UpdateUserProfileAPI(SerializerVersionMixin, UpdateAPIView):
    """
        Open API endpoint to update UserProfile details
        support ~> [PATCH]
    """
    
    version_map = {
        'v1': UpdateProfileSerializerV1,
    }
    permission_classes = [IsAuthenticated]
    lookup_field = 'user__username'
    lookup_url_kwarg = 'username'

    def get_queryset(self):
        username = self.request.user.username
        return Profile.objects.filter(user__username=username)
    
    def update(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            query = self.get_queryset()
            if request.user.username == query[0].user.username:
                return super().update(request, *args, **kwargs)
            return Response(data={"error": "User is not allowed to perform this action"}, status=status.HTTP_401_UNAUTHORIZED)
    

