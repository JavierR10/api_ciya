from django.db import models
from django.utils import timezone

from apps.laboratory.src.models.laboratory import Laboratory
from apps.laboratory.src.models.software import Software

class LaboratorySoftware(models.Model):
    id_labsof = models.AutoField(primary_key=True)
    fk_id_lab = models.ForeignKey(Laboratory, models.DO_NOTHING, db_column='fk_id_lab', blank=True, null=True)
    fk_id_sof = models.ForeignKey(Software, models.DO_NOTHING, db_column='fk_id_sof', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'laboratorios\".\"laboratorio_software'

