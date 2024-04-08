from django.db import models
from apps.bonding.src.models.company import Company
from apps.bonding.src.models.agreement import Agreement
from apps.bonding.src.models.linkingProcess import LinkingProcess

class GroupVin(models.Model):
    id_grupo = models.AutoField(primary_key=True)
    nombre_grupo = models.CharField(max_length=250)
    numero_grupo = models.TextField()
    estado_grupo = models.CharField(max_length=15)
    fecha_creacion_grupo = models.DateTimeField()
    fecha_actualizacion_grupo = models.DateTimeField()
    usuario_creacion_grupo = models.CharField(max_length=250)
    usuario_actualizacion_grupo = models.CharField(max_length=250)
    fk_id_prov = models.ForeignKey(LinkingProcess, models.DO_NOTHING, db_column='fk_id_prov', blank=True, null=True)
    fk_id_con = models.ForeignKey(Agreement, models.DO_NOTHING, db_column='fk_id_con', blank=True, null=True)
    fk_id_cur = models.IntegerField(blank=True, null=True)
    fk_id_emp = models.ForeignKey(Company, models.DO_NOTHING, db_column='fk_id_emp', blank=True, null=True)

    class Meta:
        db_table = 'vinculacion\".\"grupovin'