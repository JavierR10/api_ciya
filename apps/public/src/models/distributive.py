from django.db import models


class Distributive(models.Model):
    id_dis = models.AutoField(primary_key=True)
    fk_id_per = models.IntegerField(blank=True, null=True)
    fk_id_mat = models.IntegerField(blank=True, null=True)
    fk_id_doc = models.IntegerField(blank=True, null=True)
    paralelo_dis = models.CharField(max_length=2, blank=True, null=True)
    silabo_dis = models.CharField(max_length=200, blank=True, null=True)
    fecha_creacion_dis = models.DateField(blank=True, null=True)
    fecha_actualizacion_dis = models.DateField(blank=True, null=True)
    usuario = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        db_table = 'public\".\"distributivo'
