from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#filter
from apps.academic.src.api.globalFilter.filter.filters import NewsFilterFolder
#MODELOS
from apps.academic.src.models.news import News
#serializers
from apps.academic.src.api.news.serializers import NewsSerializers
#paginado
from apps.pagination import CustomPagination

class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializers
    queryset = News.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterFolder
    pagination_class = CustomPagination

