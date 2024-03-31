from django.db import models
from django.utils import timezone
from .base import BaseModel

class Laboratory(BaseModel):
    id_lab = models.AutoField(primary_key=True)
    nombre_lab = models.CharField(max_length=255)
    descripcion_lab = models.CharField(max_length=1000)
    fotografia1_lab = models.CharField(max_length=255)
    fotografia2_lab = models.CharField(max_length=255)
    fk_docente_responsable_lab = models.IntegerField()
    fk_administrativo_responsable_lab = models.IntegerField()
    fecha_creacion_lab = models.DateTimeField(auto_now=True)
    fecha_actualizacion_lab = models.DateTimeField(auto_now=True)
    usuario_creacion_lab = models.CharField(max_length=255)
    usuario_actualizacion_lab = models.CharField(max_length=255)
    tipo_lab = models.CharField(max_length=255)
    ubicacion_lab = models.CharField(max_length=300)
    color_lab = models.CharField(max_length=15)
    fk_administrativo_responsable_secundario_lab = models.IntegerField()
    siglas_lab = models.CharField(max_length=255)
    paralelo_guia = models.CharField(max_length=255)

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
        db_table = 'laboratorios\".\"laboratorio'

