from rest_framework import viewsets
#MODELOS
from apps.ciya.src.models.university import universidad

#serializers
from apps.ciya.src.api.university.serializers import UniversitySerializers

class UniversityViewSet(viewsets.ModelViewSet):
    queryset = universidad.objects.all()
    serializer_class = UniversitySerializers
