from rest_framework import viewsets
#MODELOS
from apps.laboratory.src.models.practicalGuide import PracticalGuide

#serializers
from apps.laboratory.src.api.practicalGuide.serializers import PracticalGuideSerializers

class PracticalGuideViewSet(viewsets.ModelViewSet):
    serializer_class = PracticalGuideSerializers
    
    def get_queryset(self):
        return PracticalGuide.objects.all()
