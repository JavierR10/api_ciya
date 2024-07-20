from django.db import models

class Type(models.Model):
    id_tip = models.AutoField(primary_key=True)
    nombre_tip = models.TextField(blank=True, null=True)
    siglas_tip = models.CharField(max_length=50, blank=True, null=True)
    estado_tip = models.IntegerField(blank=True, null=True)
    fecha_creacion_tip = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_tip = models.DateTimeField(blank=True, null=True)
    usuario_creacion_tip = models.CharField(max_length=255, blank=True, null=True)
    usuario_actualizacion_tip = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'vinculacion\".\"tipo'