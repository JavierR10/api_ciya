from rest_framework import viewsets
#MODELOS
from apps.laboratory.src.models.reservationType import ReservationType

#serializers
from apps.laboratory.src.api.reservationType.serializers import ReservationTypeSerializers

class ReservationTypeViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationTypeSerializers
    
    def get_queryset(self):
        return ReservationType.objects.filter(deleted_at__isnull=True)
