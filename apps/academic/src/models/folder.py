from django.db import models
from django.utils import timezone
from .base import BaseModel

class Folder(BaseModel):
    id_carp = models.AutoField(primary_key=True)
    parend_id_carp = models.IntegerField()
    nombre_carp = models.CharField(max_length=100)
    fk_id_usu =  models.IntegerField()
    descripcion_carp = models.CharField(max_length=100)
    fecha_cierre_carp =  models.DateField(auto_now=True)
    hora_cierre_carp =  models.TimeField(auto_now=True)
    estado_carp = models.CharField(max_length=20)
    disposicion_carp = models.CharField(max_length=20)
    fecha_creacion_carp = models.DateTimeField(auto_now=True)
    fecha_actualizacion_carp =  models.DateTimeField(auto_now=True)

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
        db_table = 'academico\".\"carpeta'

