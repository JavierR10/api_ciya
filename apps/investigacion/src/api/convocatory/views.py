from rest_framework import viewsets
#MODELOS
from apps.investigacion.src.models.convocatory import Convocatory

#serializers
from apps.investigacion.src.api.convocatory.serializers import ConvocatorySerializers

class ConvocatoryViewSet(viewsets.ModelViewSet):
    serializer_class = ConvocatorySerializers
    
    def get_queryset(self):
        return Convocatory.objects.all()
