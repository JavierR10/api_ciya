from django.db import models
from django.utils import timezone
from django.core.validators import EmailValidator
from django.contrib.auth.hashers import make_password
from .base import BaseModel
from apps.public.src.models.profile import profile

class users(BaseModel):
    id_usu = models.AutoField(primary_key=True)
    correo_usu = models.EmailField(max_length=40, validators=[EmailValidator], unique=True)
    password_usu = models.TextField()
    nombre_usu = models.CharField(max_length=40)
    apellido_usu = models.CharField(max_length=40)
    fk_id_prf = models.ForeignKey(profile, on_delete=models.RESTRICT, to_field='id_prf')  
    estado_usu = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        if not self.id_usu:
            self.password_usu = make_password(self.password_usu)
        super(users, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
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
        db_table = 'users'
