from rest_framework import viewsets
#MODELOS
from apps.laboratory.src.models.reservation import Reservation

#serializers
from apps.laboratory.src.api.reservation.serializers import ReservationSerializers

class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializers
    
    def get_queryset(self):
        return Reservation.objects.filter(deleted_at__isnull=True)
