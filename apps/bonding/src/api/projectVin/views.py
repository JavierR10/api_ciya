from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
#filter
from apps.bonding.src.api.globalFilter.filter.filters import NewsFilterProjectVin
#####
#MODELOS
from apps.bonding.src.models.projectVin import ProjectVin
#serializers
from apps.bonding.src.api.projectVin.serializers import ProjectVinSerializers

class ProjectVinViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectVinSerializers
    queryset = ProjectVin.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterProjectVin
    pagination_class = CustomPagination
