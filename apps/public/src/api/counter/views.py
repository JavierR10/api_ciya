from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.public.src.api.globalFilter.filter.filters import NewsFilterCounter
#MODELOS
from apps.public.src.models.counter import Counter

#serializers
from apps.public.src.api.counter.serializers import CounterSerializers

class CounterViewSet(viewsets.ModelViewSet):
    serializer_class = CounterSerializers
    queryset = Counter.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterCounter
    pagination_class = CustomPagination