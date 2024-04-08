from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
#filter
from apps.bonding.src.api.globalFilter.filter.filters import NewsFilterIntegranteVin
#####
#MODELOS
from apps.bonding.src.models.integranteVIn import IntegranteVin
#serializers
from apps.bonding.src.api.integranteVIn.serializers import IntegranteVinSerializers

class IntegranteVinViewSet(viewsets.ModelViewSet):
    serializer_class = IntegranteVinSerializers
    queryset = IntegranteVin.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterIntegranteVin
    pagination_class = CustomPagination
