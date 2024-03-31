from django.db import models
from django.core.validators import EmailValidator
from django.utils import timezone
from .base import BaseModel

class Teacher(BaseModel):
    id_doc = models.AutoField(primary_key=True)
    cedula_doc = models.CharField(max_length=15)
    primer_apellido_doc = models.CharField(max_length=100)
    segundo_apellido_doc = models.CharField(max_length=100)
    nombre_doc = models.CharField(max_length=150)
    abreviatura_titulo_doc = models.CharField(max_length=150)
    fotografia_doc = models.CharField(max_length=255)
    perfil_profesional_doc = models.TextField()
    telefono_doc = models.CharField(max_length=15)
    email_doc = models.CharField(max_length=150, validators=[EmailValidator], unique=True)
    oficina_doc = models.CharField(max_length=250)
    facebook_doc = models.CharField(max_length=500)
    twitter_doc = models.CharField(max_length=500)
    pagina_web_doc = models.CharField(max_length=500)
    fk_id_car = models.IntegerField()
    fecha_creacion_doc = models.DateTimeField(auto_now=True)
    fecha_actualizacion_doc = models.DateTimeField(auto_now=True)
    usuario_creacion_doc = models.CharField(max_length=100)
    usuario_actualizacion_doc = models.CharField(max_length=100)
    fk_id_usu = models.IntegerField()
    linkedin_doc = models.CharField(max_length=150)
    sexo_doc = models.CharField(max_length=15)

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
        db_table = 'public\".\"docente'
