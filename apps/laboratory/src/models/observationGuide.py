from django.db import models
from django.utils import timezone
from .base import BaseModel
from apps.laboratory.src.models.practicalGuide import PracticalGuide

class ObservationGuide(BaseModel):
    id_observacion = models.AutoField(primary_key=True)
    fecha_observacion = models.DateTimeField(auto_now=True)
    detalle_observacion = models.TextField()
    fk_id_guia = models.ForeignKey(PracticalGuide, on_delete=models.RESTRICT, to_field='id_guia')
    fk_id_doc = models.IntegerField()
    estado_observaciones_guia_practica = models.CharField(max_length=50)

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
        db_table = 'laboratorios\".\"observacion_guia'

