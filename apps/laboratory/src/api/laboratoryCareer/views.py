from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.laboratory.src.api.globalFilter.filter.filters import NewsFilterLaboratoryCareer
#MODELOS
from apps.laboratory.src.models.laboratoryCareer import LaboratoryCareer

#serializers
from apps.laboratory.src.api.laboratoryCareer.serializers import LaboratoryCareerSerializers

class LaboratoryCareerViewSet(viewsets.ModelViewSet):
    serializer_class = LaboratoryCareerSerializers
    queryset = LaboratoryCareer.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterLaboratoryCareer
    pagination_class = CustomPagination