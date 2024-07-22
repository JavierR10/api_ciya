from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
#filter
from apps.bonding.src.api.globalFilter.filter.filters import NewsFilterCompany
#####
#MODELOS
from apps.bonding.src.models.company import Company
#serializers
from apps.bonding.src.api.company.serializers import CompanySerializers

class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializers
    queryset = Company.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterCompany
    pagination_class = CustomPagination
