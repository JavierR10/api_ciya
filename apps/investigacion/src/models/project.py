from django.db import models
from apps.investigacion.src.models.projectType import ProjectType

class Project(models.Model):
    id_pro = models.AutoField(primary_key=True)
    nombre_pro = models.CharField(max_length=1000, blank=True, null=True)
    fk_id_car = models.IntegerField(blank=True, null=True)
    fk_id_doc = models.IntegerField(blank=True, null=True)
    grupo_investigacion_pro = models.CharField(max_length=1000, blank=True, null=True)
    programa_pro = models.CharField(max_length=1000, blank=True, null=True)
    fk_id_tip = models.ForeignKey(ProjectType, models.DO_NOTHING, db_column='fk_id_tip', blank=True, null=True)
    fecha_aprobacion_pro = models.DateField(blank=True, null=True)
    fk_id_lin = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'investigacion\".\"proyecto'

