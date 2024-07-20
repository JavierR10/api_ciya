from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.public.src.api.globalFilter.filter.filters import NewsFilterFaculty
#MODELOS
from apps.public.src.models.faculty import Faculty

#serializers
from apps.public.src.api.faculty.serializers import FacultySerializers

class FacultyViewSet(viewsets.ModelViewSet):
    serializer_class = FacultySerializers
    queryset = Faculty.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterFaculty
    pagination_class = CustomPagination