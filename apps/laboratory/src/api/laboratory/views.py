from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.laboratory.src.api.globalFilter.filter.filters import NewsFilterLaboratory
#MODELOS
from apps.laboratory.src.models.laboratory import Laboratory

#serializers
from apps.laboratory.src.api.laboratory.serializers import LaboratorySerializers

class LaboratoryViewSet(viewsets.ModelViewSet):
    serializer_class = LaboratorySerializers
    queryset = Laboratory.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterLaboratory
    pagination_class = CustomPagination