from django.db import models


class Area(models.Model):
    id_area = models.AutoField(primary_key=True)
    nombre_area = models.CharField(max_length=500, blank=True, null=True)
    descripcion_area = models.CharField(max_length=2500, blank=True, null=True)
    imagen_area = models.CharField(max_length=1500, blank=True, null=True)
    fecha_creacion_area = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_area = models.DateTimeField(blank=True, null=True)
    usuario_creacion_area = models.CharField(max_length=255, blank=True, null=True)
    usuario_actualizacion_area = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'laboratorios\".\"area'

