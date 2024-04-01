from rest_framework import viewsets
#MODELOS
from apps.laboratory.src.models.software import Software

#serializers
from apps.laboratory.src.api.software.serializers import SoftwareSerializers

class SoftwareViewSet(viewsets.ModelViewSet):
    serializer_class = SoftwareSerializers
    
    def get_queryset(self):
        return Software.objects.all()
