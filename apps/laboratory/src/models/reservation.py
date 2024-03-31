from django.db import models
from django.utils import timezone
from .base import BaseModel

class Reservation(BaseModel):
    id_res = models.AutoField(primary_key=True)
    fk_id_tipres = models.CharField(max_length=100)
    fk_id_doc = models.IntegerField()
    fk_id_lab =  models.IntegerField()
    fk_id_area = models.IntegerField()
    fk_id_guia = models.IntegerField()
    tema_res = models.TextField()
    comentario_res = models.TextField()
    estado_res = models.CharField(max_length=100)
    fecha_hora_res = models.DateTimeField(auto_now=True)
    duracion_res = models.IntegerField()
    numero_participantes_res = models.IntegerField()
    descripcion_participantes_res = models.TextField()
    materiales_res = models.TextField()
    fecha_creacion_res = models.DateTimeField(auto_now=True)
    fecha_actualizacion_res = models.DateTimeField(auto_now=True)
    usuario_creacion_res = models.CharField(max_length=255)
    usuario_actualizacion_res = models.CharField(max_length=255)
    fecha_hora_fin_res = models.DateTimeField(auto_now=True)
    observaciones_finales_res = models.TextField()
    asistencia_res = models.CharField(max_length=50)
    guia_adjunta_res = models.CharField(max_length=500)
    curso_res = models.CharField(max_length=150)
    materia_res = models.CharField(max_length=150)
    fk_id_car = models.IntegerField()
    paralelo_res = models.CharField(max_length=150)
    tipo_texto_res = models.CharField(max_length=150)
    fk_id_usu = models.IntegerField()
    software_res = models.CharField(max_length=255)
    tipo_res = models.CharField(max_length=20)
    pedidodocente_res = models.IntegerField()


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
        db_table = 'laboratorios\".\"reserva'

