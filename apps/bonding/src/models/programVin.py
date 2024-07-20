from django.db import models

class ProgramVin(models.Model):
    id_prog = models.AutoField(primary_key=True)
    nombre_prog = models.CharField(max_length=250)
    descripcion_prog = models.TextField()
    estado_prog = models.CharField(max_length=15)
    fecha_creacion_prog = models.DateTimeField()
    fecha_actualizacion_prog = models.DateTimeField()
    usuario_creacion_prog = models.CharField(max_length=250)
    usuario_actualizacion_prog = models.CharField(max_length=250)
    fk_id_fac = models.IntegerField(blank=True, null=True)
    archivo_prog = models.CharField(max_length=1500, blank=True, null=True)

    class Meta:
        db_table = 'vinculacion\".\"programavin'