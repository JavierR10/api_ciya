from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
#filter
from apps.academic.src.api.globalFilter.filter.filters import NewsFilterAssociatedDocument
#####
#MODELOS
from apps.academic.src.models.associatedDocument import AssociatedDocument
#serializers
from apps.academic.src.api.associatedDocument.serializers import AssociatedDocumentSerializers

class AssociatedDocumentViewSet(viewsets.ModelViewSet):
    serializer_class = AssociatedDocumentSerializers
    queryset = AssociatedDocument.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterAssociatedDocument
    pagination_class = CustomPagination
