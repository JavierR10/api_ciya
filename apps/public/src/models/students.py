from django.db import models
from apps.public.src.models.faculty import Faculty
from apps.public.src.models.collegeCareer import CollegeCareer
from apps.public.src.models.period import Period


class Students(models.Model):
    id_est = models.AutoField(primary_key=True)
    cedula_est = models.CharField(max_length=100, blank=True, null=True)
    primer_apellido_est = models.CharField(max_length=100, blank=True, null=True)
    segundo_apellido_est = models.CharField(max_length=100, blank=True, null=True)
    nombre_est = models.CharField(max_length=100, blank=True, null=True)
    email_est = models.CharField(max_length=100, blank=True, null=True)
    telefono_est = models.CharField(max_length=100, blank=True, null=True)
    ciclo_est = models.CharField(max_length=100, blank=True, null=True)
    fk_id_fac = models.ForeignKey(Faculty, models.DO_NOTHING, db_column='fk_id_fac', blank=True, null=True)
    fk_id_car = models.ForeignKey(CollegeCareer, models.DO_NOTHING, db_column='fk_id_car', blank=True, null=True)
    celular_est = models.CharField(max_length=100, blank=True, null=True)
    genero_est = models.CharField(max_length=100, blank=True, null=True)
    estado_civil_est = models.CharField(max_length=100, blank=True, null=True)
    etnia_est = models.CharField(max_length=100, blank=True, null=True)
    discapacidad_est = models.CharField(max_length=100, blank=True, null=True)
    provincia_est = models.CharField(max_length=150, blank=True, null=True)
    ciudad_est = models.CharField(max_length=150, blank=True, null=True)
    parroquia_est = models.CharField(max_length=500, blank=True, null=True)
    direccion_est = models.CharField(max_length=500, blank=True, null=True)
    fk_id_per = models.ForeignKey(Period, models.DO_NOTHING, db_column='fk_id_per', blank=True, null=True)
    fk_id_usu = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'public\".\"estudiantes'
