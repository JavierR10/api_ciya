from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
#filter
from apps.bonding.src.api.globalFilter.filter.filters import NewsFilterAgreement
#####
#MODELOS
from apps.bonding.src.models.agreement import Agreement
#serializers
from apps.bonding.src.api.agreement.serializers import AgreementSerializers

class AgreementViewSet(viewsets.ModelViewSet):
    serializer_class = AgreementSerializers
    queryset = Agreement.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterAgreement
    pagination_class = CustomPagination
