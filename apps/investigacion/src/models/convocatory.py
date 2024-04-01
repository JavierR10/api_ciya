from django.db import models

class Convocatory(models.Model):
    id_conv = models.AutoField(primary_key=True)
    documento_conv = models.CharField(max_length=500, blank=True, null=True)
    estado_conv = models.CharField(max_length=500, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'investigacion\".\"convocatoria'

