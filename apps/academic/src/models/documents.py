from django.db import models
from django.utils import timezone
from .base import BaseModel

class Documents(BaseModel):
    id_doc = models.AutoField(primary_key=True)
    fk_id_carp = models.IntegerField()
    nombre_doc = models.CharField(max_length=100)
    documento_doc = models.CharField(max_length=100)
    descripcion_doc = models.CharField(max_length=200)
    fecha_entrega_doc = models.DateField()
    fecha_creacion_doc  = models.DateTimeField(auto_now=True)
    fecha_actualizacion_doc = models.DateTimeField(auto_now=True)
    usuario_creacion_doc = models.CharField(max_length=255)
    usuario_actualizacion_doc = models.CharField(max_length=255)
    fk_id_usu = models.IntegerField()
    publico_doc = models.CharField(max_length=10)
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
        db_table = 'academico\".\"documento'

