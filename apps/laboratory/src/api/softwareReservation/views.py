from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.laboratory.src.api.globalFilter.filter.filters import NewsFilterSoftwareReservation
#MODELOS
from apps.laboratory.src.models.softwareReservation import SoftwareReservation

#serializers
from apps.laboratory.src.api.softwareReservation.serializers import SoftwareReservationSerializers

class SoftwareReservationViewSet(viewsets.ModelViewSet):
    serializer_class = SoftwareReservationSerializers
    queryset = SoftwareReservation.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterSoftwareReservation
    pagination_class = CustomPagination