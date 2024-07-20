from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.public.src.api.globalFilter.filter.filters import NewsFilterPermissions
#MODELOS
from apps.public.src.models.permissions import Permissions

#serializers
from apps.public.src.api.permissions.serializers import PermissionsSerializers

class PermissionsViewSet(viewsets.ModelViewSet):
    serializer_class = PermissionsSerializers
    queryset = Permissions.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterPermissions
    pagination_class = CustomPagination