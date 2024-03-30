from django.db import models
from .base import BaseModel
from django.utils import timezone
from apps.ciya.src.models.profile import profile
from apps.ciya.src.models.usuario import users

class profileUsers(BaseModel):
    id_perusu = models.AutoField(primary_key=True)
    fk_id_per = models.ForeignKey(profile, on_delete=models.RESTRICT, to_field='id_prf')
    fk_id_usu = models.ForeignKey(users, on_delete=models.RESTRICT, to_field='id_usu')

    def delete(self):
        self.deleted_at = timezone.now()  # Establecer la fecha de eliminación
        self.save()

    class Meta:
        db_table = 'perfil_usuario'
    
