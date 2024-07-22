from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
#filter
from apps.bonding.src.api.globalFilter.filter.filters import NewsFilterScheduleVin
#####
#MODELOS
from apps.bonding.src.models.scheduleVin import ScheduleVin
#serializers
from apps.bonding.src.api.scheduleVin.serializers import ScheduleVinSerializers

class ScheduleVinViewSet(viewsets.ModelViewSet):
    serializer_class = ScheduleVinSerializers
    queryset = ScheduleVin.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterScheduleVin
    pagination_class = CustomPagination
