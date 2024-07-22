from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.laboratory.src.api.globalFilter.filter.filters import NewsFilterArea

#MODELOS
from apps.laboratory.src.models.area import Area

#serializers
from apps.laboratory.src.api.area.serializers import AreaSerializers

class AreaViewSet(viewsets.ModelViewSet):
    serializer_class = AreaSerializers
    queryset = Area.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterArea
    pagination_class = CustomPagination