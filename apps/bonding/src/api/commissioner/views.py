from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
#filter
from apps.bonding.src.api.globalFilter.filter.filters import NewsFilterCommissioner
#####
#MODELOS
from apps.bonding.src.models.commissioner import Commissioner
#serializers
from apps.bonding.src.api.commissioner.serializers import CommissionerSerializers

class CommissionerViewSet(viewsets.ModelViewSet):
    serializer_class = CommissionerSerializers
    queryset = Commissioner.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterCommissioner
    pagination_class = CustomPagination
