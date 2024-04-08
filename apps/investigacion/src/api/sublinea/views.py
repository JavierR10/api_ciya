from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.investigacion.src.api.globalFilter.filter.filters import NewsFilterSublinea
#MODELOS
from apps.investigacion.src.models.sublinea import Sublinea

#serializers
from apps.investigacion.src.api.sublinea.serializers import SublineaSerializers

class SublineaViewSet(viewsets.ModelViewSet):
    serializer_class = SublineaSerializers
    queryset = Sublinea.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterSublinea
    pagination_class = CustomPagination