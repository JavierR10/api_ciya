from rest_framework import viewsets
#MODELOS
from apps.public.src.models.collegeCareer import CollegeCareer

#serializers
from apps.public.src.api.collegeCareer.serializers import CollegeCareerSerializers

class CollegeCareerViewSet(viewsets.ModelViewSet):
    serializer_class = CollegeCareerSerializers
    
    def get_queryset(self):
        return CollegeCareer.objects.filter(deleted_at__isnull=True)