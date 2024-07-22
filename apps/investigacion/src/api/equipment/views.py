from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.investigacion.src.api.globalFilter.filter.filters import NewsFilterEquipment

#MODELOS
from apps.investigacion.src.models.equipment import Equipment

#serializers
from apps.investigacion.src.api.equipment.serializers import EquipmentSerializers

class EquipmentViewSet(viewsets.ModelViewSet):
    serializer_class = EquipmentSerializers
    queryset = Equipment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterEquipment
    pagination_class = CustomPagination