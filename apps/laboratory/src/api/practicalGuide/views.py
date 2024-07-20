from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.laboratory.src.api.globalFilter.filter.filters import NewsFilterPracticalGuide
#MODELOS
from apps.laboratory.src.models.practicalGuide import PracticalGuide

#serializers
from apps.laboratory.src.api.practicalGuide.serializers import PracticalGuideSerializers

class PracticalGuideViewSet(viewsets.ModelViewSet):
    serializer_class = PracticalGuideSerializers
    queryset = PracticalGuide.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterPracticalGuide
    pagination_class = CustomPagination
