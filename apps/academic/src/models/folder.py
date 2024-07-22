from django.db import models

class Folder(models.Model):
    id_carp = models.AutoField(primary_key=True)
    parend_id_carp = models.IntegerField(blank=True, null=True)
    nombre_carp = models.CharField(max_length=100, blank=True, null=True)
    fk_id_usu = models.IntegerField(blank=True, null=True)
    descripcion_carp = models.CharField(max_length=200, blank=True, null=True)
    fecha_cierre_carp = models.DateField(blank=True, null=True)
    hora_cierre_carp = models.TimeField(blank=True, null=True)
    estado_carp = models.CharField(max_length=20, blank=True, null=True)
    disposicion_carp = models.CharField(max_length=20, blank=True, null=True)
    fecha_creacion_carp = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_carp = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'academico\".\"carpeta'

