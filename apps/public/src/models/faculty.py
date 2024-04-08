from django.db import models

class Faculty(models.Model):
    id_fac = models.AutoField(primary_key=True)
    nombre_fac = models.CharField(max_length=100, blank=True, null=True)
    siglas_fac = models.CharField(max_length=10, blank=True, null=True)
    fk_decano_fac = models.IntegerField(blank=True, null=True)
    fk_vicedecano_fac = models.IntegerField(blank=True, null=True)
    correo_fac = models.CharField(max_length=50, blank=True, null=True)
    telefono_fac = models.CharField(max_length=10, blank=True, null=True)
    fecha_creacion_fac = models.DateField(blank=True, null=True)
    fecha_actualizacion_fac = models.DateField(blank=True, null=True)
    usuario_creacion_fac = models.CharField(max_length=100, blank=True, null=True)
    usuario_actualizacion_fac = models.CharField(max_length=100, blank=True, null=True)
    mision_fac = models.CharField(max_length=500, blank=True, null=True)
    vision_fac = models.CharField(max_length=500, blank=True, null=True)
    logo_fac = models.CharField(max_length=1500, blank=True, null=True)

    class Meta:
        db_table = 'public\".\"facultad'
