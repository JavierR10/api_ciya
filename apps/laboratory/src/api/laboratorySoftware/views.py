from rest_framework import viewsets
#MODELOS
from apps.laboratory.src.models.laboratorySoftware import LaboratorySoftware

#serializers
from apps.laboratory.src.api.laboratorySoftware.serializers import LaboratorySoftwareSerializers

class LaboratorySoftwareViewSet(viewsets.ModelViewSet):
    serializer_class = LaboratorySoftwareSerializers
    
    def get_queryset(self):
        return LaboratorySoftware.objects.all()
