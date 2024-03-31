from django.db import models
from django.utils import timezone
from .base import BaseModel
from apps.public.src.models.collegeCareer import CollegeCareer
from apps.public.src.models.teacher import Teacher
from apps.investigacion.src.models.sublinea import Sublinea
from apps.investigacion.src.models.linea import Linea

class PracticalGuide(BaseModel):
    id_guia = models.AutoField(primary_key=True)
    numero_practica_guia = models.CharField(max_length=255)
    tema_guia = models.CharField(max_length=255)
    fecha_inicial_guia =  models.DateTimeField(auto_now=True)
    fecha_final_guia = models.DateTimeField(auto_now=True)
    archivo_guia = models.CharField(max_length=255)
    fk_id_doc = models.IntegerField()
    objetivo_guia = models.TextField()
    instrucciones_guia = models.TextField()
    resultados_esperados_guia = models.TextField()
    bibliografia_guia = models.TextField()
    fk_id_lab = models.IntegerField()
    fecha_creacion_guia = models.DateTimeField(auto_now=True)
    fecha_actualizacion_guia = models.DateTimeField(auto_now=True)
    usuario_creacion_guia = models.CharField(max_length=255)
    usuario_actualizacion_guia = models.CharField(max_length=255)
    fk_id_per = models.IntegerField()
    fk_id_cur = models.IntegerField()
    fk_id_mat = models.IntegerField()
    fk_id_malla = models.IntegerField()
    area_guia = models.TextField()
    medidas_guia = models.TextField()
    instrumentos_guia = models.TextField()
    trabajopreparatorio_guia = models.TextField()
    actividades_guia = models.TextField()
    informacion_guia = models.TextField()
    fk_laboratorista_aprobado = models.ForeignKey(Teacher, on_delete=models.RESTRICT, to_field='id_doc', related_name='docente')
    fk_director_aprobado = models.ForeignKey(Teacher, on_delete=models.RESTRICT, to_field='id_doc',  related_name='guiapractica')
    fecha_laboratorista_aprobado = models.DateTimeField(auto_now=True)
    fecha_director_aprobado = models.DateTimeField(auto_now=True)
    hora_guia = models.IntegerField()
    fk_id_lin = models.ForeignKey(Linea, on_delete=models.RESTRICT, to_field='id_lin', related_name='linea')
    fk_id_sub = models.ForeignKey(Sublinea, on_delete=models.RESTRICT, to_field='id_sub', related_name='bunlinea')
    fk_id_coordinador_id_doc = models.CharField(max_length=250)
    fk_id_car = models.ForeignKey(CollegeCareer, on_delete=models.RESTRICT, to_field='id_car', related_name='carrera')
    paralelo_guia = models.CharField(max_length=5)
    metodologia_guia = models.TextField()
    estado_guia_practica = models.CharField(max_length=50)


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
        db_table = 'laboratorios\".\"guiapractica'

