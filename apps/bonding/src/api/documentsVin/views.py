from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
#filter
from apps.bonding.src.api.globalFilter.filter.filters import NewsFilterDocumentsVin
#####
#MODELOS
from apps.bonding.src.models.documentsVin import DocumentsVin
#serializers
from apps.bonding.src.api.documentsVin.serializers import DocumentsVinSerializers

class DocumentsVinViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentsVinSerializers
    queryset = DocumentsVin.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterDocumentsVin
    pagination_class = CustomPagination
