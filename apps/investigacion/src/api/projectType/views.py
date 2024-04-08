from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.investigacion.src.api.globalFilter.filter.filters import NewsFilterProjectType
#MODELOS
from apps.investigacion.src.models.projectType import ProjectType

#serializers
from apps.investigacion.src.api.projectType.serializers import ProjectTypeSerializers

class ProjectTypeViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectTypeSerializers
    
    queryset = ProjectType.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterProjectType
    pagination_class = CustomPagination

