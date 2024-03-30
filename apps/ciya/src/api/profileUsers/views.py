from rest_framework import viewsets
#MODELOS
from apps.ciya.src.models.profileUsers import profileUsers

#serializers
from apps.ciya.src.api.profileUsers.serializers import ProfileUsersSerializers

class ProfileUsersViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileUsersSerializers

    def get_queryset(self):
        return profileUsers.objects.filter(deleted_at__isnull=True)