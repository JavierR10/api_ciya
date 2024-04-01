from rest_framework import viewsets
#MODELOS
from apps.laboratory.src.models.observationGuide import ObservationGuide

#serializers
from apps.laboratory.src.api.observationGuide.serializers import ObservationGuideSerializers

class ObservationGuideViewSet(viewsets.ModelViewSet):
    serializer_class = ObservationGuideSerializers
    
    def get_queryset(self):
        return ObservationGuide.objects.all()
