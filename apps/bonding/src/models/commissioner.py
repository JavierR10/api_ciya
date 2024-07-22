from django.db import models

class Commissioner(models.Model):
    id_comi = models.AutoField(primary_key=True)
    estado_comi = models.CharField(max_length=15)
    fecha_creacion_comi = models.DateTimeField()
    fecha_actualizacion_comi = models.DateTimeField()
    usuario_creacion_comi = models.CharField(max_length=250)
    usuario_actualizacion_comi = models.CharField(max_length=250)
    fk_id_doc = models.IntegerField(blank=True, null=True)
    fk_id_per = models.IntegerField(blank=True, null=True)
    fk_id_car = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'vinculacion\".\"comicionado'

