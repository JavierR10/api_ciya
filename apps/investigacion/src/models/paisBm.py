from django.db import models
class PaisBm(models.Model):
    id_bm = models.AutoField(primary_key=True)
    nombre_bm = models.CharField(max_length=100, blank=True, null=True)
    continente_bm = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'investigacion\".\"pais_bm'

