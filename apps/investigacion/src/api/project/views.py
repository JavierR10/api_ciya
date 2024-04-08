from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.investigacion.src.api.globalFilter.filter.filters import NewsFilterProject
#MODELOS
from apps.investigacion.src.models.project import Project

#serializers
from apps.investigacion.src.api.project.serializers import ProjectSerializers

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializers
    queryset = Project.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterProject
    pagination_class = CustomPagination

