from django.db import models


class LaboratoryCareer(models.Model):
    id_labcar = models.AutoField(primary_key=True)
    fk_id_lab = models.IntegerField(blank=True, null=True)
    fk_id_car = models.IntegerField(blank=True, null=True)
    fecha_creacion_labcar = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_labcar = models.DateTimeField(blank=True, null=True)
    usuario_creacion_labcar = models.CharField(max_length=255, blank=True, null=True)
    usuario_actualizacion_labcar = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'laboratorios\".\"laboratorio_carrera'

