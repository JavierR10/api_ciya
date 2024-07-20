from django.db import models

class Agreement(models.Model):
    id_con = models.AutoField(primary_key=True)
    documento_con = models.CharField(max_length=1500, blank=True, null=True)
    fecha_inicio_con = models.DateField(blank=True, null=True)
    fecha_fin_con = models.DateField(blank=True, null=True)
    fk_id_emp = models.IntegerField()
    fecha_creacion_con = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_con = models.DateTimeField(blank=True, null=True)
    usuario_creacion_con = models.CharField(max_length=255, blank=True, null=True)
    usuario_actualizacion_con = models.CharField(max_length=255, blank=True, null=True)
    tipo_con = models.CharField(max_length=50, blank=True, null=True)
    estado_con = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'vinculacion\".\"convenio'

