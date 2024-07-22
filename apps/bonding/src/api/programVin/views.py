from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
#filter
from apps.bonding.src.api.globalFilter.filter.filters import NewsFilterProgramVin
#####
#MODELOS
from apps.bonding.src.models.programVin import ProgramVin
#serializers
from apps.bonding.src.api.programVin.serializers import ProgramVinSerializers

class ProgramVinViewSet(viewsets.ModelViewSet):
    serializer_class = ProgramVinSerializers
    queryset = ProgramVin.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterProgramVin
    pagination_class = CustomPagination
