from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
#filter
from apps.bonding.src.api.globalFilter.filter.filters import NewsFilterType
#####
#MODELOS
from apps.bonding.src.models.type import Type
#serializers
from apps.bonding.src.api.type.serializers import TypeSerializers

class TypeViewSet(viewsets.ModelViewSet):
    serializer_class = TypeSerializers
    queryset = Type.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterType
    pagination_class = CustomPagination
