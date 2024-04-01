from django.db import models
from apps.investigacion.src.models.group import Group

class Equipment(models.Model):
    id_equ = models.AutoField(primary_key=True)
    fk_id_doc = models.IntegerField(blank=True, null=True)
    fk_id_gru = models.ForeignKey(Group, models.DO_NOTHING, db_column='fk_id_gru', blank=True, null=True)

    
    class Meta:
        managed = False
        db_table = 'investigacion\".\"equipo'

