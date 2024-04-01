from django.db import models
from django.utils import timezone
from .base import BaseModel

class News(BaseModel):
    id_not = models.AutoField(primary_key=True)
    titulo_not = models.CharField(max_length=100)
    descripcion_not = models.TextField()
    imagen_not = models.CharField(max_length=100)
    estado_not = models.CharField(max_length=20)
    fecha_creacion_not = models.DateTimeField(auto_now=True)

    def delete(self):
        self.deleted_at = timezone.now()  # Establecer la fecha de eliminación
        self.save()

        
        # Actualizar objetos relacionados
        related_objects = self._meta.related_objects
        for related_object in related_objects:
            related_model = related_object.related_model
            related_name = related_object.get_accessor_name()
            related_field_name = related_object.field.name
            related_queryset = getattr(self, related_name).all()
            related_queryset.update(deleted_at=timezone.now())
    
    class Meta:
        db_table = 'academico\".\"noticia'

