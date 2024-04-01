from rest_framework import viewsets
#MODELOS
from apps.investigacion.src.models.equipment import Equipment

#serializers
from apps.investigacion.src.api.equipment.serializers import EquipmentSerializers

class EquipmentViewSet(viewsets.ModelViewSet):
    serializer_class = EquipmentSerializers
    
    def get_queryset(self):
        return Equipment.objects.all()
