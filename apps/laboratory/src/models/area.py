from django.db import models
from django.utils import timezone
from .base import BaseModel

class Area(BaseModel):
    id_area = models.AutoField(primary_key=True)
    nombre_area = models.CharField(max_length=100)
    descripcion_area = models.TextField()
    imagen_area =  models.TextField()
    fecha_creacion_area = models.DateTimeField(auto_now=True)
    fecha_actualizacion_area = models.DateTimeField(max_length=255)
    usuario_creacion_area = models.CharField(max_length=255)
    usuario_actualizacion_area = models.CharField(max_length=255)
   

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
        db_table = 'laboratorios\".\"area'

