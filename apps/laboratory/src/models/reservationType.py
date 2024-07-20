from django.db import models


class ReservationType(models.Model):
    id_tipres = models.AutoField(primary_key=True)
    nombre_tipres = models.CharField(max_length=100, blank=True, null=True)
    estado_tipres = models.CharField(max_length=50, blank=True, null=True)
    fecha_creacion_tipres = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_tipres = models.DateTimeField(blank=True, null=True)
    usuario_creacion_tipres = models.CharField(max_length=255, blank=True, null=True)
    usuario_actualizacion_tipres = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'laboratorios\".\"tipo_reserva'

