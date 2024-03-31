from django.db import models
from django.utils import timezone
from .base import BaseModel

class Software(BaseModel):
    id_sof = models.AutoField(primary_key=True)
    nombre_sof = models.CharField(max_length=100)
    tipolicencia_sof = models.CharField(max_length=100)
    cantidad_sof =  models.CharField(max_length=100)
    unidad_sof = models.CharField(max_length=50)
    costounitario_sof = models.CharField(max_length=50)
    costototal_sof = models.CharField(max_length=50)
    aplicaciones_sof = models.CharField(max_length=100)
    caracteristicas_sof = models.CharField(max_length=100)
    fecha_creacion_sof = models.DateTimeField(auto_now=True)
    fecha_actualizacion_sof = models.DateTimeField(auto_now=True)
    usuario_creacion_sof = models.CharField(max_length=255)
    usuario_actualizacion_sof = models.CharField(max_length=255)
    imagen_sof = models.CharField(max_length=255)
    fecha_caducidad_sof = models.DateTimeField(null=True)
    enlace_sof = models.TextField()

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
        db_table = 'laboratorios\".\"software'

