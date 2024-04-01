from django.db import models

class Sublinea(models.Model):
    id_sub = models.AutoField(primary_key=True)
    fk_id_car = models.IntegerField(blank=True, null=True)
    nombre_sub = models.TextField(blank=True, null=True)
    descripcion_sub = models.TextField(blank=True, null=True)
    estado_sub = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'investigacion\".\"sublinea'

