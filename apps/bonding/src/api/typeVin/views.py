from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
#filter
from apps.bonding.src.api.globalFilter.filter.filters import NewsFilterTypeVin
#####
#MODELOS
from apps.bonding.src.models.typeVin import TypeVin
#serializers
from apps.bonding.src.api.typeVin.serializers import TypeVinSerializers

class TypeVinViewSet(viewsets.ModelViewSet):
    serializer_class = TypeVinSerializers
    queryset = TypeVin.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterTypeVin
    pagination_class = CustomPagination
