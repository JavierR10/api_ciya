from django.db import models
from apps.bonding.src.models.projectVin import ProjectVin

class DocumentsVin(models.Model):
    id_doc = models.AutoField(primary_key=True)
    nombre_doc = models.CharField(max_length=250)
    descripcion_doc = models.CharField(max_length=250)
    estado_doc = models.CharField(max_length=15)
    fecha_creacion_doc = models.DateTimeField()
    fecha_actualizacion_doc = models.DateTimeField()
    usuario_creacion_doc = models.CharField(max_length=250)
    usuario_actualizacion_doc = models.CharField(max_length=250)
    documento_doc = models.CharField(max_length=250)
    fk_id_proy = models.ForeignKey(ProjectVin, models.DO_NOTHING, db_column='fk_id_proy', blank=True, null=True)

    class Meta:
        db_table = 'vinculacion\".\"documentovin'