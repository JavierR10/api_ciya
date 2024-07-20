from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
#paginado
from apps.pagination import CustomPagination
from apps.public.src.api.globalFilter.filter.filters import NewsFilterCourse
#MODELOS
from apps.public.src.models.course import Course

#serializers
from apps.public.src.api.course.serializers import CourseSerializers

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializers
    queryset = Course.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterCourse
    pagination_class = CustomPagination