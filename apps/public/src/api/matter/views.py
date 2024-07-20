from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.public.src.api.globalFilter.filter.filters import NewsFilterMatter
#MODELOS
from apps.public.src.models.matter import Matter

#serializers
from apps.public.src.api.matter.serializers import MatterSerializers

class MatterViewSet(viewsets.ModelViewSet):
    serializer_class = MatterSerializers
    queryset = Matter.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterMatter
    pagination_class = CustomPagination