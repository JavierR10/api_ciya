from django.db import models
from django.utils import timezone
from .base import BaseModel

class LaboratoryCareer(BaseModel):
    id_labcar = models.AutoField(primary_key=True)
    fk_id_lab = models.IntegerField()
    fk_id_car = models.IntegerField()
    fecha_creacion_labcar = models.DateTimeField(auto_now=True)
    fecha_actualizacion_labcar = models.DateTimeField(auto_now=True)
    usuario_creacion_labcar = models.CharField(max_length=255)
    usuario_actualizacion_labcar = models.CharField(max_length=255)

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
        db_table = 'laboratorios\".\"laboratorio_carrera'

