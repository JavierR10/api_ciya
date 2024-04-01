from django.db import models

class PaisSv(models.Model):
    id_sv = models.AutoField(primary_key=True)
    nombre_sv = models.CharField(max_length=100, blank=True, null=True)
    continente_sv = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'investigacion\".\"pais_sv'

