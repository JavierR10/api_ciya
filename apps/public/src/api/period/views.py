from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.public.src.api.globalFilter.filter.filters import NewsFilterPeriod
#MODELOS
from apps.public.src.models.period import Period

#serializers
from apps.public.src.api.period.serializers import PeriodSerializers

class PeriodViewSet(viewsets.ModelViewSet):
    serializer_class = PeriodSerializers
    queryset = Period.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterPeriod
    pagination_class = CustomPagination