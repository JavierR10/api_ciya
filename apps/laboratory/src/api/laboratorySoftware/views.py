from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.laboratory.src.api.globalFilter.filter.filters import NewsFilterLaboratorySoftware
#MODELOS
from apps.laboratory.src.models.laboratorySoftware import LaboratorySoftware

#serializers
from apps.laboratory.src.api.laboratorySoftware.serializers import LaboratorySoftwareSerializers

class LaboratorySoftwareViewSet(viewsets.ModelViewSet):
    serializer_class = LaboratorySoftwareSerializers
    queryset = LaboratorySoftware.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterLaboratorySoftware
    pagination_class = CustomPagination
