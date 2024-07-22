from django.db import models
from apps.bonding.src.models.programVin import ProgramVin

class ProjectVin(models.Model):
    id_proy = models.AutoField(primary_key=True)
    nombre_proy = models.CharField(max_length=250)
    descripcion_proy = models.TextField()
    estado_proy = models.CharField(max_length=15)
    fecha_creacion_proy = models.DateTimeField()
    fecha_actualizacion_proy = models.DateTimeField()
    usuario_creacion_proy = models.CharField(max_length=250)
    usuario_actualizacion_proy = models.CharField(max_length=250)
    fk_id_car = models.IntegerField(blank=True, null=True)
    fk_id_per = models.IntegerField(blank=True, null=True)
    fk_id_prog = models.ForeignKey(ProgramVin, models.DO_NOTHING, db_column='fk_id_prog', blank=True, null=True)

    class Meta:
        db_table = 'vinculacion\".\"proyectovin'