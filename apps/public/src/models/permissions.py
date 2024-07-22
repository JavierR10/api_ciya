from django.db import models
from apps.public.src.models.security import Security
from apps.public.src.models.profile import profile

class Permissions(models.Model):
    id_prm = models.AutoField(primary_key=True)
    fk_id_seg = models.ForeignKey(Security, models.DO_NOTHING, db_column='fk_id_seg', blank=True, null=True)
    fk_id_prf = models.ForeignKey(profile, models.DO_NOTHING, db_column='fk_id_prf', blank=True, null=True)
    permiso_visualizar_prm = models.SmallIntegerField(blank=True, null=True)
    permiso_agregar = models.SmallIntegerField(blank=True, null=True)
    permiso_editar = models.SmallIntegerField(blank=True, null=True)
    permiso_eliminar = models.SmallIntegerField(blank=True, null=True)
    permiso_imprimir = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'public\".\"permisos'
