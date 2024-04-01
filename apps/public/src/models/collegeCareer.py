from django.db import models
from django.core.validators import EmailValidator

from apps.public.src.models.teacher import Teacher

class CollegeCareer(models.Model):
    id_car = models.AutoField(primary_key=True)
    fk_id_fac = models.IntegerField()
    nombre_car = models.CharField(max_length=200, blank=True, null=True)
    siglas_car = models.CharField(max_length=50, blank=True, null=True)
    fk_director_doc = models.CharField(max_length=100, blank=True, null=True)
    foto_logo_car = models.CharField(max_length=200, blank=True, null=True)
    telefono_car = models.CharField(max_length=15, blank=True, null=True)
    email_car = models.CharField(max_length=150, blank=True, null=True, validators=[EmailValidator], unique=True)
    fecha_creacion_car = models.DateField(blank=True, null=True)
    fecha_actualizacion_car = models.DateField(blank=True, null=True)
    usuario_creacion_car = models.CharField(max_length=100, blank=True, null=True)
    usuario_actualizacion_car = models.CharField(max_length=100, blank=True, null=True)
    mision_car = models.CharField(max_length=1000, blank=True, null=True)
    vision_car = models.CharField(max_length=1000, blank=True, null=True)
    fk_dir_doc = models.ForeignKey(Teacher, models.DO_NOTHING, db_column='fk_dir_doc', blank=True, null=True)

    class Meta:
        db_table = 'public\".\"carrera'
