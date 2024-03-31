from rest_framework import viewsets
#MODELOS
from apps.laboratory.src.models.areaLaboratory import AreaLaboratory

#serializers
from apps.laboratory.src.api.areaLaboratory.serializers import AreaLaboratorySerializers

class AreaLaboratoryViewSet(viewsets.ModelViewSet):
    serializer_class = AreaLaboratorySerializers
    
    def get_queryset(self):
        return AreaLaboratory.objects.filter(deleted_at__isnull=True)
