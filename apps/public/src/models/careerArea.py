from django.db import models

from apps.public.src.models.teacher import Teacher
from apps.public.src.models.collegeCareer import CollegeCareer

class CareerArea(models.Model):
    id_area_car = models.AutoField(primary_key=True)
    nombre_area_car = models.CharField(max_length=250, blank=True, null=True)
    descripcion_area_car = models.TextField(blank=True, null=True)
    foto_area_car = models.CharField(max_length=1500, blank=True, null=True)
    fk_id_car = models.ForeignKey(CollegeCareer, models.DO_NOTHING, db_column='fk_id_car', blank=True, null=True)
    fk_id_doc = models.ForeignKey(Teacher, models.DO_NOTHING, db_column='fk_id_doc', blank=True, null=True)

    class Meta:
        db_table = 'public\".\"area_carrera'
