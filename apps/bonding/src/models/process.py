from django.db import models
from apps.bonding.src.models.type import Type

class Process(models.Model):
    id_proc = models.AutoField(primary_key=True)
    fk_id_per = models.IntegerField(blank=True, null=True)
    fk_id_tip = models.ForeignKey(Type, models.DO_NOTHING, db_column='fk_id_tip', blank=True, null=True)
    fk_id_con = models.IntegerField(blank=True, null=True)
    fk_id_doc = models.IntegerField(blank=True, null=True)
    tema_proc = models.TextField(blank=True, null=True)
    fecha_creacion_proc = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_proc = models.DateTimeField(blank=True, null=True)
    usuario_creacion_proc = models.CharField(max_length=255, blank=True, null=True)
    usuario_actualizacion_proc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'vinculacion\".\"proceso'