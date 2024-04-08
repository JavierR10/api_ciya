from django.db import models
from apps.bonding.src.models.agreement import Agreement

class CareerAgreement(models.Model):
    id_con_car = models.AutoField(primary_key=True)
    fk_id_con = models.ForeignKey(Agreement, models.DO_NOTHING, db_column='fk_id_con', blank=True, null=True)
    fk_id_car = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'vinculacion\".\"convenio_carrera'

