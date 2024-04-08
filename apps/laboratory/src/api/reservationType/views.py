from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.laboratory.src.api.globalFilter.filter.filters import NewsFilterReservationType
#MODELOS
from apps.laboratory.src.models.reservationType import ReservationType

#serializers
from apps.laboratory.src.api.reservationType.serializers import ReservationTypeSerializers

class ReservationTypeViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationTypeSerializers
    queryset = ReservationType.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterReservationType
    pagination_class = CustomPagination