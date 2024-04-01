from rest_framework import viewsets
#MODELOS
from apps.laboratory.src.models.laboratoryCareer import LaboratoryCareer

#serializers
from apps.laboratory.src.api.laboratoryCareer.serializers import LaboratoryCareerSerializers

class LaboratoryCareerViewSet(viewsets.ModelViewSet):
    serializer_class = LaboratoryCareerSerializers
    
    def get_queryset(self):
        return LaboratoryCareer.objects.all()
