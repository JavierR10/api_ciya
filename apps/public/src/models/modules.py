from django.db import models

class Module(models.Model):
    id_mod = models.AutoField(primary_key=True)
    nombre_mod = models.CharField(max_length=150, blank=True, null=True)
    descripcion_mod = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        db_table = 'public\".\"modulos'
