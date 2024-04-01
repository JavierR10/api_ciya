from django.db import models


class profile(models.Model):
    id_prf = models.AutoField(primary_key=True)
    nombre_prf = models.CharField(max_length=150, blank=True, null=True)
    descripcion_prf = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'public\".\"perfil'
