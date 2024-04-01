from django.db import models

from apps.public.src.models.profile import profile
from apps.public.src.models.usuario import users

class profileUsers(models.Model):
    id_perusu = models.AutoField(primary_key=True)
    fk_id_per = models.ForeignKey(profile, models.DO_NOTHING, db_column='fk_id_per', blank=True, null=True)
    fk_id_usu = models.ForeignKey(users, models.DO_NOTHING, db_column='fk_id_usu', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'public\".\"perfil_usuario'

