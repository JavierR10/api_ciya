from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#filter
from apps.academic.src.api.globalFilter.filter.filters import NewsFilterDocuments
#MODELOS
from apps.academic.src.models.documents import Documents
#serializers
from apps.academic.src.api.documents.serializers import DocumentsSerializers
#paginado
from apps.pagination import CustomPagination
class DocumentsViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentsSerializers
    queryset = Documents.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterDocuments
    pagination_class = CustomPagination

