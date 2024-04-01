from rest_framework import viewsets
#MODELOS
from apps.laboratory.src.models.softwareReservation import SoftwareReservation

#serializers
from apps.laboratory.src.api.softwareReservation.serializers import SoftwareReservationSerializers

class SoftwareReservationViewSet(viewsets.ModelViewSet):
    serializer_class = SoftwareReservationSerializers
    
    def get_queryset(self):
        return SoftwareReservation.objects.all()
