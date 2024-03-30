from django.db import models
from .base import BaseModel
from django.utils import timezone
from apps.public.src.models.profile import profile
from apps.public.src.models.usuario import users

class profileUsers(BaseModel):
    id_perusu = models.AutoField(primary_key=True)
    fk_id_per = models.ForeignKey(profile, on_delete=models.RESTRICT, to_field='id_prf')
    fk_id_usu = models.ForeignKey(users, on_delete=models.RESTRICT, to_field='id_usu')

    def delete(self):
        self.deleted_at = timezone.now()  # Establecer la fecha de eliminación
        self.save()


        # Actualizar objetos relacionados
        related_objects = self._meta.related_objects
        for related_object in related_objects:
            related_model = related_object.related_model
            related_name = related_object.get_accessor_name()
            related_field_name = related_object.field.name
            related_queryset = getattr(self, related_name).all()
            related_queryset.update(deleted_at=timezone.now())

    class Meta:
        db_table = 'perfil_usuario'
    
