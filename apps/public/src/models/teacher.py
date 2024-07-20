from django.db import models
from django.core.validators import EmailValidator


class Teacher(models.Model):
    id_doc = models.AutoField(primary_key=True)
    cedula_doc = models.CharField(max_length=15, blank=True, null=True)
    primer_apellido_doc = models.CharField(max_length=100, blank=True, null=True)
    segundo_apellido_doc = models.CharField(max_length=100, blank=True, null=True)
    nombre_doc = models.CharField(max_length=150, blank=True, null=True)
    abreviatura_titulo_doc = models.CharField(max_length=150, blank=True, null=True)
    fotografia_doc = models.CharField(max_length=255, blank=True, null=True)
    perfil_profesional_doc = models.TextField(blank=True, null=True)
    telefono_doc = models.CharField(max_length=15, blank=True, null=True)
    email_doc = models.CharField(max_length=150, blank=True, null=True,  validators=[EmailValidator], unique=True)
    oficina_doc = models.CharField(max_length=250, blank=True, null=True)
    facebook_doc = models.CharField(max_length=500, blank=True, null=True)
    twitter_doc = models.CharField(max_length=500, blank=True, null=True)
    pagina_web_doc = models.CharField(max_length=500, blank=True, null=True)
    fk_id_car = models.IntegerField(blank=True, null=True)
    fecha_creacion_doc = models.DateField(blank=True, null=True)
    fecha_actualizacion_doc = models.DateField(blank=True, null=True)
    usuario_creacion_doc = models.CharField(max_length=100, blank=True, null=True)
    usuario_actualizacion_doc = models.CharField(max_length=100, blank=True, null=True)
    fk_id_usu = models.IntegerField(blank=True, null=True)
    linkedin_doc = models.CharField(max_length=150, blank=True, null=True)
    sexo_doc = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'public\".\"docente'
