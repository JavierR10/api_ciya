from django.db import models
from apps.public.src.models.collegeCareer import CollegeCareer
from apps.public.src.models.academicMesh import AcademicMesh
from apps.public.src.models.teacher import Teacher

class Matter(models.Model):
    id_mat = models.AutoField(primary_key=True)
    fk_id_cur = models.IntegerField(blank=True, null=True)
    nombre_mat = models.CharField(max_length=200, blank=True, null=True)
    descripcion_mat = models.CharField(max_length=900, blank=True, null=True)
    fecha_creacion_mat = models.DateField(blank=True, null=True)
    fecha_actualizacion_mat = models.DateField(blank=True, null=True)
    usuario_creacion_mat = models.CharField(max_length=100, blank=True, null=True)
    usuario_actualizacion_mat = models.CharField(max_length=100, blank=True, null=True)
    fk_id_car = models.ForeignKey(CollegeCareer, models.DO_NOTHING, db_column='fk_id_car', blank=True, null=True)
    fk_id_malla = models.ForeignKey(AcademicMesh, models.DO_NOTHING, db_column='fk_id_malla', blank=True, null=True)
    codigo_mat = models.CharField(max_length=15, blank=True, null=True)
    fk_id_doc = models.ForeignKey(Teacher, models.DO_NOTHING, db_column='fk_id_doc', blank=True, null=True)
    tipo_mat = models.CharField(max_length=200, blank=True, null=True)
    class Meta:
        db_table = 'public\".\"materia'
