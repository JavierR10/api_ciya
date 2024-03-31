from django.db import models
from django.utils import timezone
from .base import BaseModel

class ReservationType(BaseModel):
    id_tipres = models.AutoField(primary_key=True)
    nombre_tipres = models.CharField(max_length=100)
    estado_tipres = models.CharField(max_length=50)
    fecha_creacion_tipres =  models.DateTimeField(auto_now=True)
    fecha_actualizacion_tipres = models.DateTimeField(auto_now=True)
    usuario_creacion_tipres = models.CharField(max_length=255)
    usuario_actualizacion_tipres = models.CharField(max_length=255)

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
        db_table = 'laboratorios\".\"tipo_reserva'

