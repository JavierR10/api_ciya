from django.db import models
from django.core.validators import EmailValidator
from django.utils import timezone
from .base import BaseModel
from apps.public.src.models.teacher import Teacher

class CollegeCareer(BaseModel):
    id_car = models.AutoField(primary_key=True)
    fk_id_fac = models.IntegerField()
    nombre_car = models.CharField(max_length=200)
    siglas_car = models.CharField(max_length=50)
    fk_director_doc = models.CharField(max_length=100)
    foto_logo_car = models.CharField(max_length=200)
    telefono_car = models.CharField(max_length=150)
    email_car = models.CharField(max_length=150, validators=[EmailValidator], unique=True)
    fecha_creacion_car = models.DateTimeField(auto_now=True)
    fecha_actualizacion_car = models.DateTimeField(auto_now=True)
    usuario_creacion_car = models.CharField(max_length=100)
    usuario_actualizacion_car = models.CharField(max_length=100)
    mision_car = models.TextField()
    vision_car = models.TextField()
    fk_dir_doc = models.ForeignKey(Teacher, on_delete=models.RESTRICT, to_field='id_doc')

    
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
        db_table = 'public\".\"carrera'
