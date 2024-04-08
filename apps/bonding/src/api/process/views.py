from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
#filter
from apps.bonding.src.api.globalFilter.filter.filters import NewsFilterProcess
#####
#MODELOS
from apps.bonding.src.models.process import Process
#serializers
from apps.bonding.src.api.process.serializers import ProcessSerializers

class ProcessViewSet(viewsets.ModelViewSet):
    serializer_class = ProcessSerializers
    queryset = Process.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterProcess
    pagination_class = CustomPagination
