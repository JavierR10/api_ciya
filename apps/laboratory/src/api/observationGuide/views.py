from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.laboratory.src.api.globalFilter.filter.filters import NewsFilterObservationGuide

#MODELOS
from apps.laboratory.src.models.observationGuide import ObservationGuide

#serializers
from apps.laboratory.src.api.observationGuide.serializers import ObservationGuideSerializers

class ObservationGuideViewSet(viewsets.ModelViewSet):
    serializer_class = ObservationGuideSerializers
    
    queryset = ObservationGuide.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterObservationGuide
    pagination_class = CustomPagination
