from rest_framework import viewsets
#MODELOS
from apps.investigacion.src.models.sublinea import Sublinea

#serializers
from apps.investigacion.src.api.sublinea.serializers import SublineaSerializers

class SublineaViewSet(viewsets.ModelViewSet):
    serializer_class = SublineaSerializers
    
    def get_queryset(self):
        return Sublinea.objects.filter(deleted_at__isnull=True)
