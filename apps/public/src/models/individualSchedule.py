from django.db import models

class IndividualSchedule(models.Model):
    id_horaindi = models.AutoField(primary_key=True)
    archivo_horaindi = models.CharField(max_length=255, blank=True, null=True)
    fk_id_doc = models.IntegerField(blank=True, null=True)
    fk_id_per = models.IntegerField(blank=True, null=True)
    fecha_creacion_horaindi = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_horaindi = models.DateTimeField(blank=True, null=True)
    usuario_creacion_horaindi = models.CharField(max_length=100, blank=True, null=True)
    usuario_actualizacion_horaindi = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'public\".\"horario_individual'
