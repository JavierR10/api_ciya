from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.investigacion.src.api.globalFilter.filter.filters import NewsFilterLinea

#MODELOS
from apps.investigacion.src.models.linea import Linea

#serializers
from apps.investigacion.src.api.linea.serializers import LineaSerializers

class LineaViewSet(viewsets.ModelViewSet):
    serializer_class = LineaSerializers
    queryset = Linea.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterLinea
    pagination_class = CustomPagination