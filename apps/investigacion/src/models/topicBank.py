from django.db import models
from django.utils import timezone
from .base import BaseModel
from apps.investigacion.src.models.linea import Linea

class TopicBank(BaseModel):
    id_ban = models.AutoField(primary_key=True)
    fk_id_doc = models.IntegerField()
    fk_id_lin = models.ForeignKey(Linea, on_delete=models.RESTRICT, to_field='id_lin')
    fk_id_sub = models.IntegerField()
    tema_ban = models.CharField(max_length=500)
    descripcion_ban = models.TextField()
    archivo_adjunto_ban = models.TextField()
    fecha_creacion_ban = models.DateTimeField(auto_now=True)
    fecha_actualizacion_ban = models.DateTimeField(auto_now=True)
    usuario_creacion_ban = models.CharField(max_length=255)
    usuario_actualizacion_ban = models.CharField(max_length=255)
    validacion_ban = models.CharField(max_length=100)
    estado_ban = models.CharField(max_length=50)

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
        db_table = 'investigacion\".\"banco_temas'

