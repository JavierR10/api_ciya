from django.db import models

class TypeVin(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    nombre_tipo = models.CharField(max_length=250)
    siglas_tipo = models.CharField(max_length=250)
    descripcion_tipo = models.TextField()
    estado_tipo = models.CharField(max_length=15)
    fecha_creacion_tipo = models.DateTimeField()
    fecha_actualizacion_tipo = models.DateTimeField()
    usuario_creacion_tipo = models.CharField(max_length=250)
    usuario_actualizacion_tipo = models.CharField(max_length=250)

    class Meta:
        db_table = 'vinculacion\".\"tipovin'