from rest_framework import viewsets
#MODELOS
from apps.ciya.src.models.profile import profile

#serializers
from apps.ciya.src.api.profile.serializers import ProfileSerializers

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializers
    
    def get_queryset(self):
        return profile.objects.filter(deleted_at__isnull=True)
