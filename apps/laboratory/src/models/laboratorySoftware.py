from django.db import models
from django.utils import timezone
from .base import BaseModel
from apps.laboratory.src.models.laboratory import Laboratory
from apps.laboratory.src.models.software import Software

class LaboratorySoftware(BaseModel):
    id_labsof = models.AutoField(primary_key=True)
    fk_id_lab = models.ForeignKey(Laboratory, on_delete=models.RESTRICT, to_field='id_lab')
    fk_id_sof = models.ForeignKey(Software, on_delete=models.RESTRICT, to_field='id_sof')

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
        db_table = 'laboratorios\".\"laboratorio_software'

