from rest_framework import viewsets
#MODELOS
from apps.investigacion.src.models.linea import Linea

#serializers
from apps.investigacion.src.api.linea.serializers import LineaSerializers

class LineaViewSet(viewsets.ModelViewSet):
    serializer_class = LineaSerializers
    
    def get_queryset(self):
        return Linea.objects.all()
