from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.investigacion.src.api.globalFilter.filter.filters import NewsFilterGroup

#MODELOS
from apps.investigacion.src.models.group import Group

#serializers
from apps.investigacion.src.api.group.serializers import GroupSerializers

class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializers
    queryset = Group.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterGroup
    pagination_class = CustomPagination

