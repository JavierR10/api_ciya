from django.db import models
from apps.investigacion.src.models.linea import Linea

class TopicBank(models.Model):
    id_ban = models.AutoField(primary_key=True)
    fk_id_doc = models.IntegerField(blank=True, null=True)
    fk_id_lin = models.ForeignKey(Linea, models.DO_NOTHING, db_column='fk_id_lin', blank=True, null=True)
    fk_id_sub = models.IntegerField(blank=True, null=True)
    tema_ban = models.CharField(max_length=500, blank=True, null=True)
    descripcion_ban = models.TextField(blank=True, null=True)
    archivo_adjunto_ban = models.CharField(max_length=1500, blank=True, null=True)
    fecha_creacion_ban = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_ban = models.DateTimeField(blank=True, null=True)
    usuario_creacion_ban = models.CharField(max_length=255, blank=True, null=True)
    usuario_actualizacion_ban = models.CharField(max_length=255, blank=True, null=True)
    validacion_ban = models.CharField(max_length=100, blank=True, null=True)
    estado_ban = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'investigacion\".\"banco_temas'

