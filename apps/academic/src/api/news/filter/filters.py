import django_filters
from apps.academic.src.models.news import News

class NewsFilter(django_filters.FilterSet):
    class Meta:
        model = News
        fields = {
            'id_not': ['exact'],
            'titulo_not': ['icontains'],
            'descripcion_not': ['icontains'],
            'imagen_not': ['exact'],
            'estado_not': ['exact'],
            'fecha_creacion_not': ['lte', 'gte'],
        }
