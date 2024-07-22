from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.investigacion.src.api.globalFilter.filter.filters import NewsFilterConvocatory

#MODELOS
from apps.investigacion.src.models.convocatory import Convocatory

#serializers
from apps.investigacion.src.api.convocatory.serializers import ConvocatorySerializers

class ConvocatoryViewSet(viewsets.ModelViewSet):
    serializer_class = ConvocatorySerializers
    queryset = Convocatory.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterConvocatory
    pagination_class = CustomPagination
