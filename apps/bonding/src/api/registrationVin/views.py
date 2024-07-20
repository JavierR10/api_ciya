from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
#filter
from apps.bonding.src.api.globalFilter.filter.filters import NewsFilterRegistrationVin
#####
#MODELOS
from apps.bonding.src.models.registrationVin import RegistrationVin
#serializers
from apps.bonding.src.api.registrationVin.serializers import RegistrationVinSerializers

class RegistrationVinViewSet(viewsets.ModelViewSet):
    serializer_class = RegistrationVinSerializers
    queryset = RegistrationVin.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterRegistrationVin
    pagination_class = CustomPagination
