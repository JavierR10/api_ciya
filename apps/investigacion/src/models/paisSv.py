from django.db import models
from django.utils import timezone
from .base import BaseModel

class PaisSv(BaseModel):
    id_sv = models.AutoField(primary_key=True)
    nombre_sv = models.CharField(max_length=100)
    continente_sv = models.CharField(max_length=100)

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
        db_table = 'investigacion\".\"pais_sv'

