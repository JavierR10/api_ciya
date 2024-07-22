from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
#filter
from apps.bonding.src.api.globalFilter.filter.filters import NewsFilterDocuments
#####
#MODELOS
from apps.bonding.src.models.documets import Documents
#serializers
from apps.bonding.src.api.documets.serializers import DocumentsSerializers

class DocumentsViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentsSerializers
    queryset = Documents.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterDocuments
    pagination_class = CustomPagination
