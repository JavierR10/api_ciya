from rest_framework import viewsets
#MODELOS
from apps.laboratory.src.models.area import Area

#serializers
from apps.laboratory.src.api.area.serializers import AreaSerializers

class AreaViewSet(viewsets.ModelViewSet):
    serializer_class = AreaSerializers
    
    def get_queryset(self):
        return Area.objects.filter(deleted_at__isnull=True)
