from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
#filter
from apps.bonding.src.api.globalFilter.filter.filters import NewsFilterGroupVin
#####
#MODELOS
from apps.bonding.src.models.groupVin import GroupVin
#serializers
from apps.bonding.src.api.groupVin.serializers import GroupVinSerializers

class GroupVinViewSet(viewsets.ModelViewSet):
    serializer_class = GroupVinSerializers
    queryset = GroupVin.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterGroupVin
    pagination_class = CustomPagination
