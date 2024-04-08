from django.db import models
from apps.public.src.models.collegeCareer import CollegeCareer


class StudentRepresentatives(models.Model):
    id_repest = models.AutoField(primary_key=True)
    primer_apellido_repest = models.CharField(max_length=100, blank=True, null=True)
    segundo_apellido_repest = models.CharField(max_length=100, blank=True, null=True)
    nombre_repest = models.CharField(max_length=100, blank=True, null=True)
    correo_repest = models.CharField(max_length=100, blank=True, null=True)
    telefono_repest = models.CharField(max_length=100, blank=True, null=True)
    fk_id_car = models.ForeignKey(CollegeCareer, models.DO_NOTHING, db_column='fk_id_car', blank=True, null=True)
    foto_repest = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'public\".\"representantes_estudiantiles'
