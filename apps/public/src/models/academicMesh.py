from django.db import models

class AcademicMesh(models.Model):
    id_malla = models.AutoField(primary_key=True)
    fk_id_car = models.IntegerField(blank=True, null=True)
    nombre_malla = models.CharField(max_length=255, blank=True, null=True)
    descripcion_malla = models.CharField(max_length=255, blank=True, null=True)
    estado_malla = models.CharField(max_length=25, blank=True, null=True)
    archivo_malla = models.CharField(max_length=255, blank=True, null=True)
    fecha_creacion_malla = models.DateField(blank=True, null=True)
    fecha_actualizacion_malla = models.DateField(blank=True, null=True)
    usuario_creacion_malla = models.CharField(max_length=255, blank=True, null=True)
    usuario_actualizacion_malla = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'public\".\"malla_academica'
