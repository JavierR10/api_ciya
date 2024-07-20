from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.laboratory.src.api.globalFilter.filter.filters import NewsFilterAreaLaboratory

#MODELOS
from apps.laboratory.src.models.areaLaboratory import AreaLaboratory

#serializers
from apps.laboratory.src.api.areaLaboratory.serializers import AreaLaboratorySerializers

class AreaLaboratoryViewSet(viewsets.ModelViewSet):
    serializer_class = AreaLaboratorySerializers
    queryset = AreaLaboratory.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterAreaLaboratory
    pagination_class = CustomPagination
