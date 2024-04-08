from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.public.src.api.globalFilter.filter.filters import NewsFilterModule
#MODELOS
from apps.public.src.models.modules import Module

#serializers
from apps.public.src.api.modules.serializers import ModuleSerializers

class ModuleViewSet(viewsets.ModelViewSet):
    serializer_class = ModuleSerializers
    queryset = Module.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterModule
    pagination_class = CustomPagination