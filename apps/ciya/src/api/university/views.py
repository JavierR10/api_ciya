from rest_framework import viewsets
#MODELOS
from apps.ciya.src.models.university import universidad

#serializers
from apps.ciya.src.api.university.serializers import UniversitySerializers

class UniversityViewSet(viewsets.ModelViewSet):
    serializer_class = UniversitySerializers

    def get_queryset(self):
        return universidad.objects.filter(deleted_at__isnull=True)