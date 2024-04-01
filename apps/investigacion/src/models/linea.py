from django.db import models

class Linea(models.Model):
    id_lin = models.AutoField(primary_key=True)
    descripcion_lin = models.CharField(max_length=255, blank=True, null=True)
    estado_lin = models.IntegerField(blank=True, null=True)
    nombre_lin = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'investigacion\".\"linea'

