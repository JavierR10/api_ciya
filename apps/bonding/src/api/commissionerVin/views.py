from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
#filter
from apps.bonding.src.api.globalFilter.filter.filters import NewsFilterCommissionerVin
#####
#MODELOS
from apps.bonding.src.models.commissionerVin import CommissionerVin
#serializers
from apps.bonding.src.api.commissionerVin.serializers import CommissionerVinSerializers

class CommissionerVinViewSet(viewsets.ModelViewSet):
    serializer_class = CommissionerVinSerializers
    queryset = CommissionerVin.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterCommissionerVin
    pagination_class = CustomPagination
