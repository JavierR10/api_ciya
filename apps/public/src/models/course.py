from django.db import models


class Course(models.Model):
    id_cur = models.AutoField(primary_key=True)
    fk_id_malla = models.IntegerField(blank=True, null=True)
    nombre_cur = models.CharField(max_length=50, blank=True, null=True)
    fecha_creacion_cur = models.DateField(blank=True, null=True)
    fecha_actualizacion_cur = models.DateField(blank=True, null=True)
    usuario_creacion_cur = models.CharField(max_length=100, blank=True, null=True)
    usuario_actualizacion_cur = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'public\".\"curso'
