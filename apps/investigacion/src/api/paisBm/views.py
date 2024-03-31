from rest_framework import viewsets
#MODELOS
from apps.investigacion.src.models.paisBm import PaisBm

#serializers
from apps.investigacion.src.api.paisBm.serializers import PaisBmSerializers

class PaisBmViewSet(viewsets.ModelViewSet):
    serializer_class = PaisBmSerializers
    
    def get_queryset(self):
        return PaisBm.objects.filter(deleted_at__isnull=True)
