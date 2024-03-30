from rest_framework import viewsets
#MODELOS
from apps.public.src.models.profileUsers import profileUsers

#serializers
from apps.public.src.api.profileUsers.serializers import ProfileUsersSerializers

class ProfileUsersViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileUsersSerializers

    def get_queryset(self):
        return profileUsers.objects.filter(deleted_at__isnull=True)