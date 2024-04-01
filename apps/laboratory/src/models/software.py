from django.db import models
from django.utils import timezone


class Software(models.Model):
    id_sof = models.AutoField(primary_key=True)
    nombre_sof = models.CharField(max_length=100, blank=True, null=True)
    tipolicencia_sof = models.CharField(max_length=100, blank=True, null=True)
    cantidad_sof = models.CharField(max_length=100, blank=True, null=True)
    unidad_sof = models.CharField(max_length=50, blank=True, null=True)
    costounitario_sof = models.CharField(max_length=50, blank=True, null=True)
    costototal_sof = models.CharField(max_length=50, blank=True, null=True)
    aplicaciones_sof = models.CharField(max_length=1000, blank=True, null=True)
    caracteristicas_sof = models.CharField(max_length=1000, blank=True, null=True)
    fecha_creacion_sof = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_sof = models.DateTimeField(blank=True, null=True)
    usuario_creacion_sof = models.CharField(blank=True, null=True)
    usuario_actualizacion_sof = models.CharField(blank=True, null=True)
    imagen_sof = models.CharField(max_length=500, blank=True, null=True)
    fecha_caducidad_sof = models.CharField(max_length=500, blank=True, null=True)
    enlace_sof = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'laboratorios\".\"software'

