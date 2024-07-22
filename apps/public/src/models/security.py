from django.db import models
from apps.public.src.models.modules import Module


class Security(models.Model):
    id_seg = models.AutoField(primary_key=True)
    fk_id_mod = models.ForeignKey(Module, models.DO_NOTHING, db_column='fk_id_mod', blank=True, null=True)
    nombre_seg = models.CharField(max_length=150, blank=True, null=True)
    descripcion_seg = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'public\".\"seguridad'
