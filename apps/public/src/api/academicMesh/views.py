from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.public.src.api.globalFilter.filter.filters import NewsFilterAcademicMesh
#MODELOS
from apps.public.src.models.academicMesh import AcademicMesh

#serializers
from apps.public.src.api.academicMesh.serializers import AcademicMeshSerializers

class AcademicMeshViewSet(viewsets.ModelViewSet):
    serializer_class = AcademicMeshSerializers
    queryset = AcademicMesh.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterAcademicMesh
    pagination_class = CustomPagination