from django.db import models


class Laboratory(models.Model):
    id_lab = models.AutoField(primary_key=True)
    nombre_lab = models.CharField(max_length=255, blank=True, null=True)
    descripcion_lab = models.CharField(max_length=1000, blank=True, null=True)
    fotografia1_lab = models.CharField(max_length=255, blank=True, null=True)
    fotografia2_lab = models.CharField(max_length=255, blank=True, null=True)
    fk_docente_responsable_lab = models.IntegerField(blank=True, null=True)
    fk_administrativo_responsable_lab = models.IntegerField(blank=True, null=True)
    fecha_creacion_lab = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_lab = models.DateTimeField(blank=True, null=True)
    usuario_creacion_lab = models.CharField(max_length=255, blank=True, null=True)
    usuario_actualizacion_lab = models.CharField(max_length=255, blank=True, null=True)
    tipo_lab = models.CharField(max_length=255, blank=True, null=True)
    ubicacion_lab = models.CharField(max_length=300, blank=True, null=True)
    color_lab = models.CharField(max_length=15, blank=True, null=True)
    fk_administrativo_responsable_secundario_lab = models.IntegerField(blank=True, null=True)
    siglas_lab = models.CharField(max_length=15, blank=True, null=True)
    paralelo_guia = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        db_table = 'laboratorios\".\"laboratorio'

