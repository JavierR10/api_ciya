from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
#filter
from apps.bonding.src.api.globalFilter.filter.filters import NewsFilterProcessVin
#####
#MODELOS
from apps.bonding.src.models.processVin import ProcessVin
#serializers
from apps.bonding.src.api.processVin.serializers import ProcessVinSerializers

class ProcessVinProcessViewSet(viewsets.ModelViewSet):
    serializer_class = ProcessVinSerializers
    queryset = ProcessVin.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterProcessVin
    pagination_class = CustomPagination
