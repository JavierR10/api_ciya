from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.public.src.api.globalFilter.filter.filters import NewsFilterCareerArea
#MODELOS
from apps.public.src.models.careerArea import CareerArea

#serializers
from apps.public.src.api.careerArea.serializers import CareerAreaSerializers

class CareerAreaViewSet(viewsets.ModelViewSet):
    serializer_class = CareerAreaSerializers
    queryset = CareerArea.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterCareerArea
    pagination_class = CustomPagination