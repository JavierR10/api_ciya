from rest_framework import viewsets
#MODELOS
from apps.laboratory.src.models.laboratory import Laboratory

#serializers
from apps.laboratory.src.api.laboratory.serializers import LaboratorySerializers

class LaboratoryViewSet(viewsets.ModelViewSet):
    serializer_class = LaboratorySerializers
    
    def get_queryset(self):
        return Laboratory.objects.all()
