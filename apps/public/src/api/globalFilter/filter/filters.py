import django_filters
from apps.laboratory.src.models.area import Area

class NewsFilterArea(django_filters.FilterSet):
    class Meta:
        model = Area
        fields = {
            'id_area': ['exact'],
            'nombre_area': ['icontains'],
            'descripcion_area': ['icontains'],
            'imagen_area': ['icontains'],
            'fecha_creacion_area': ['exact'],
            'fecha_actualizacion_area': ['exact'],
            'usuario_creacion_area': ['icontains'],
            'usuario_actualizacion_area': ['icontains'],
        }

