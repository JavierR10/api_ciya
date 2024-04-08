from django.db import models

class Period(models.Model):
    id_per = models.AutoField(primary_key=True)
    fecha_inicio_per = models.DateField(blank=True, null=True)
    fecha_cierre_per = models.DateField(blank=True, null=True)
    rango_per = models.CharField(max_length=255)
    fecha_creacion_per = models.DateField(blank=True, null=True)
    fecha_actualizacion_per = models.DateField(blank=True, null=True)
    estado_per = models.CharField(max_length=25, blank=True, null=True)
    usuario_creacion_per = models.CharField(max_length=255, blank=True, null=True)
    usuario_actualizacion_per = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'public\".\"periodo'
