from rest_framework import viewsets
#MODELOS
from apps.academic.src.models.collaborator import Collaborator

#serializers
from apps.academic.src.api.collaborator.serializers import CollaboratorSerializers

class CollaboratorViewSet(viewsets.ModelViewSet):
    serializer_class = CollaboratorSerializers
    
    def get_queryset(self):
        return Collaborator.objects.filter(deleted_at__isnull=True)
