from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.public.src.api.globalFilter.filter.filters import NewsFilterDistributive
#MODELOS
from apps.public.src.models.distributive import Distributive

#serializers
from apps.public.src.api.distributive.serializers import DistributiveSerializers

class DistributiveViewSet(viewsets.ModelViewSet):
    serializer_class = DistributiveSerializers
    queryset = Distributive.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterDistributive
    pagination_class = CustomPagination