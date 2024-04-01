import django_filters
from apps.academic.src.models.base import BaseModel

class BaseFilter(django_filters.FilterSet):
    class Meta:
        abstract = True
        fields = {
            'flag_active': ['exact'],
            'deleted_at': ['lte', 'gte'],
            'created_at': ['lte', 'gte'],
            'updated_at': ['lte', 'gte'],
        }
