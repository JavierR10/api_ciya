from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.public.src.api.globalFilter.filter.filters import NewsFilterStudentRepresentatives
#MODELOS
from apps.public.src.models.studentRepresentatives import StudentRepresentatives

#serializers
from apps.public.src.api.studentRepresentatives.serializers import StudentRepresentativesSerializers

class StudentRepresentativesViewSet(viewsets.ModelViewSet):
    serializer_class = StudentRepresentativesSerializers
    queryset = StudentRepresentatives.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterStudentRepresentatives
    pagination_class = CustomPagination