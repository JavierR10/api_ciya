from apps.academic.src.models.news import News
from apps.academic.src.api.baseFilter.filters import BaseFilter

class NewsFilter(BaseFilter):
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
