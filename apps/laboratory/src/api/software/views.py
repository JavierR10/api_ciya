from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.laboratory.src.api.globalFilter.filter.filters import NewsFilterSoftware
#MODELOS
from apps.laboratory.src.models.software import Software

#serializers
from apps.laboratory.src.api.software.serializers import SoftwareSerializers

class SoftwareViewSet(viewsets.ModelViewSet):
    serializer_class = SoftwareSerializers
    queryset = Software.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterSoftware
    pagination_class = CustomPagination