from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
#filter
from apps.bonding.src.api.globalFilter.filter.filters import NewsFilterTutorVin
#####
#MODELOS
from apps.bonding.src.models.tutorVin import TutorVin
#serializers
from apps.bonding.src.api.tutorVin.serializers import TutorVinSerializers

class TutorVinViewSet(viewsets.ModelViewSet):
    serializer_class = TutorVinSerializers
    queryset = TutorVin.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterTutorVin
    pagination_class = CustomPagination
