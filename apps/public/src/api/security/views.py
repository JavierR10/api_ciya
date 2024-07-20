from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.public.src.api.globalFilter.filter.filters import NewsFilterSecurity
#MODELOS
from apps.public.src.models.security import Security

#serializers
from apps.public.src.api.security.serializers import SecuritySerializers

class SecurityViewSet(viewsets.ModelViewSet):
    serializer_class = SecuritySerializers
    queryset = Security.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterSecurity
    pagination_class = CustomPagination