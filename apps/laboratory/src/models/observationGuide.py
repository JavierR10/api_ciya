from django.db import models

from apps.laboratory.src.models.practicalGuide import PracticalGuide

class ObservationGuide(models.Model):
    id_observacion = models.AutoField(primary_key=True)
    fecha_observacion = models.DateTimeField(blank=True, null=True)
    detalle_observacion = models.TextField(blank=True, null=True)
    fk_id_guia = models.ForeignKey(PracticalGuide, models.DO_NOTHING, db_column='fk_id_guia', blank=True, null=True)
    fk_id_doc = models.IntegerField(blank=True, null=True)
    estado_observaciones_guia_practica = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'laboratorios\".\"observacion_guia'

