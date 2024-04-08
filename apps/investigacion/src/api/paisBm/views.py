from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.investigacion.src.api.globalFilter.filter.filters import NewsFilterPaisBm

#MODELOS
from apps.investigacion.src.models.paisBm import PaisBm

#serializers
from apps.investigacion.src.api.paisBm.serializers import PaisBmSerializers

class PaisBmViewSet(viewsets.ModelViewSet):
    serializer_class = PaisBmSerializers
    queryset = PaisBm.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterPaisBm
    pagination_class = CustomPagination