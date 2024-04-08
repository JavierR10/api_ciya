from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.public.src.api.globalFilter.filter.filters import NewsFilterIndividualSchedule
#MODELOS
from apps.public.src.models.individualSchedule import IndividualSchedule

#serializers
from apps.public.src.api.individualSchedule.serializers import IndividualScheduleSerializers

class IndividualScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = IndividualScheduleSerializers
    queryset = IndividualSchedule.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterIndividualSchedule
    pagination_class = CustomPagination