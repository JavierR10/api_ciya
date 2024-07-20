from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.laboratory.src.api.globalFilter.filter.filters import NewsFilterHoursExecuted

#MODELOS
from apps.laboratory.src.models.hoursExecuted import HoursExecuted

#serializers
from apps.laboratory.src.api.hoursExecuted.serializers import HoursExecutedSerializers

class HoursExecutedViewSet(viewsets.ModelViewSet):
    serializer_class = HoursExecutedSerializers
    queryset = HoursExecuted.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterHoursExecuted
    pagination_class = CustomPagination
