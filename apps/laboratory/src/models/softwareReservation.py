from django.db import models
from django.utils import timezone

from apps.laboratory.src.models.reservation import Reservation
from apps.laboratory.src.models.software import Software

class SoftwareReservation(models.Model):
    id_sofres = models.AutoField(primary_key=True)
    fk_id_sof = models.ForeignKey(Software, models.DO_NOTHING, db_column='fk_id_sof', blank=True, null=True)
    fk_id_res = models.ForeignKey(Reservation, models.DO_NOTHING, db_column='fk_id_res', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'laboratorios\".\"software_reserva'

