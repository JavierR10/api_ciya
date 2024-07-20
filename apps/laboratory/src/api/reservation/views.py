from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.laboratory.src.api.globalFilter.filter.filters import NewsFilterReservation
#MODELOS
from apps.laboratory.src.models.reservation import Reservation

#serializers
from apps.laboratory.src.api.reservation.serializers import ReservationSerializers

class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializers
    queryset = Reservation.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterReservation
    pagination_class = CustomPagination