from django.db import models

class Attach(models.Model):
    id_adj = models.AutoField(primary_key=True)
    fk_id_not = models.IntegerField(blank=True, null=True)
    nombre_adj = models.CharField(max_length=100, blank=True, null=True)
    documento_adj = models.CharField(max_length=100, blank=True, null=True)
    fecha_subida_adj = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'academico\".\"adjunto'

