from django.db import models

from apps.laboratory.src.models.reservation import Reservation

class HoursExecuted(models.Model):
    id_horeje = models.AutoField(primary_key=True)
    fk_id_res = models.ForeignKey(Reservation, models.DO_NOTHING, db_column='fk_id_res', blank=True, null=True)
    inicio_horeje = models.TimeField(blank=True, null=True)
    fecha_creacion_res = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_res = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'laboratorios\".\"horas_ejecutadas'

