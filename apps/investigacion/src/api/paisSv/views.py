from rest_framework import viewsets
#MODELOS
from apps.investigacion.src.models.paisSv import PaisSv

#serializers
from apps.investigacion.src.api.paisSv.serializers import PaisSvSerializers

class PaisSvViewSet(viewsets.ModelViewSet):
    serializer_class = PaisSvSerializers
    
    def get_queryset(self):
        return PaisSv.objects.all()
