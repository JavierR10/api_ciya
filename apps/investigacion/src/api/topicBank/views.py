from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.investigacion.src.api.globalFilter.filter.filters import NewsFilterTopicBank
#MODELOS
from apps.investigacion.src.models.topicBank import TopicBank

#serializers
from apps.investigacion.src.api.topicBank.serializers import TopicBankSerializers

class TopicBankViewSet(viewsets.ModelViewSet):
    serializer_class = TopicBankSerializers
    queryset = TopicBank.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterTopicBank
    pagination_class = CustomPagination

