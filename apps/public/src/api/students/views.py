from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.public.src.api.globalFilter.filter.filters import NewsFilterStudents
#MODELOS
from apps.public.src.models.students import Students

#serializers
from apps.public.src.api.students.serializers import StudentsSerializers

class StudentsViewSet(viewsets.ModelViewSet):
    serializer_class = StudentsSerializers
    queryset = Students.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterStudents
    pagination_class = CustomPagination