from django.db import models

class Company(models.Model):
    ruc_emp = models.CharField(max_length=15, blank=True, null=True)
    nombre_emp = models.CharField(max_length=500, blank=True, null=True)
    provincia_emp = models.CharField(max_length=100, blank=True, null=True)
    canton_emp = models.CharField(max_length=100, blank=True, null=True)
    direccion_emp = models.CharField(max_length=500, blank=True, null=True)
    latitud_emp = models.FloatField(blank=True, null=True)
    longitud_emp = models.FloatField(blank=True, null=True)
    telefono_emp = models.CharField(max_length=150, blank=True, null=True)
    correo_emp = models.CharField(max_length=150, blank=True, null=True)
    logo_emp = models.CharField(max_length=450, blank=True, null=True)
    tipo_emp = models.CharField(max_length=500, blank=True, null=True)
    estado_emp = models.CharField(max_length=50, blank=True, null=True)
    fecha_creacion_emp = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_emp = models.DateTimeField(blank=True, null=True)
    usuario_creacion_emp = models.CharField(max_length=255, blank=True, null=True)
    usuario_actualizacion_emp = models.CharField(max_length=255, blank=True, null=True)
    parroquia_emp = models.CharField(max_length=2500, blank=True, null=True)
    actividad_emp = models.TextField(blank=True, null=True)
    sector_economico_emp = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'vinculacion\".\"empresa'