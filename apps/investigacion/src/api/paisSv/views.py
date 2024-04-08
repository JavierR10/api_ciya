from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.investigacion.src.api.globalFilter.filter.filters import NewsFilterPaisSv
#MODELOS
from apps.investigacion.src.models.paisSv import PaisSv

#serializers
from apps.investigacion.src.api.paisSv.serializers import PaisSvSerializers

class PaisSvViewSet(viewsets.ModelViewSet):
    serializer_class = PaisSvSerializers
    queryset = PaisSv.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterPaisSv
    pagination_class = CustomPagination