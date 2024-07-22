from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
#filter
from apps.bonding.src.api.globalFilter.filter.filters import NewsFilterCareerAgreement
#####
#MODELOS
from apps.bonding.src.models.careerAgreement import CareerAgreement
#serializers
from apps.bonding.src.api.careerAgreement.serializers import CareerAgreementSerializers

class CareerAgreementViewSet(viewsets.ModelViewSet):
    serializer_class = CareerAgreementSerializers
    queryset = CareerAgreement.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterCareerAgreement
    pagination_class = CustomPagination
