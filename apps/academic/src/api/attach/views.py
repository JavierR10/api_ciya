from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
#filter
from apps.academic.src.api.globalFilter.filter.filters import NewsFilterAttach
#MODELOS
from apps.academic.src.models.attach import Attach

#serializers
from apps.academic.src.api.attach.serializers import AttachSerializers

class AttachViewSet(viewsets.ModelViewSet):
    serializer_class = AttachSerializers
    queryset = Attach.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterAttach
    pagination_class = CustomPagination
