from django.db import models

class AreaLaboratory(models.Model):
    id_labarea = models.AutoField(primary_key=True)
    fk_id_area = models.IntegerField(blank=True, null=True)
    fk_id_lab = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'laboratorios\".\"laboratorio_area'

