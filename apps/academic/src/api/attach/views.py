from rest_framework import viewsets
#MODELOS
from apps.academic.src.models.attach import Attach

#serializers
from apps.academic.src.api.attach.serializers import AttachSerializers

class AttachViewSet(viewsets.ModelViewSet):
    serializer_class = AttachSerializers
    
    def get_queryset(self):
        return Attach.objects.filter(deleted_at__isnull=True)
