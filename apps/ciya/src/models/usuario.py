from django.db import models
from django.utils import timezone
from django.core.validators import EmailValidator
from django.contrib.auth.hashers import make_password
from .base import BaseModel
from apps.ciya.src.models.profile import profile

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

    def delete(self):
        self.deleted_at = timezone.now()  # Establecer la fecha de eliminación
        self.save()

    class Meta:
        db_table = 'users'
