from django.db import models
from apps.bonding.src.models.typeVin import TypeVin

class TutorVin(models.Model):
    id_tut = models.AutoField(primary_key=True)
    estado_tut = models.CharField(max_length=15)
    fecha_creacion_tut = models.DateTimeField()
    fecha_actualizacion_tut = models.DateTimeField()
    usuario_creacion_tut = models.CharField(max_length=250)
    usuario_actualizacion_tut = models.CharField(max_length=250)
    fk_id_doc = models.IntegerField(blank=True, null=True)
    fk_id_per = models.IntegerField(blank=True, null=True)
    fk_id_tipo = models.ForeignKey(TypeVin, models.DO_NOTHING, db_column='fk_id_tipo', blank=True, null=True)
    fk_id_car = models.IntegerField(blank=True, null=True)
    fk_id_cur = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'vinculacion\".\"tutorvin'