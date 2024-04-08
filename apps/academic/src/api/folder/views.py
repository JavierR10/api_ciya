from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#filter
from apps.academic.src.api.globalFilter.filter.filters import NewsFilterFolder
#MODELOS
from apps.academic.src.models.folder import Folder
#serializers
from apps.academic.src.api.folder.serializers import FolderSerializers
#paginado
from apps.pagination import CustomPagination

class FolderViewSet(viewsets.ModelViewSet):
    serializer_class = FolderSerializers
    queryset = Folder.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterFolder
    pagination_class = CustomPagination
