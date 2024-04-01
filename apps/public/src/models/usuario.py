from django.db import models
from django.utils import timezone
from django.core.validators import EmailValidator
from django.contrib.auth.hashers import make_password
from apps.public.src.models.profile import profile

class users(models.Model):
    id_usu = models.AutoField(primary_key=True)
    correo_usu = models.CharField(max_length=50, blank=True, null=True)
    password_usu = models.CharField(max_length=250, blank=True, null=True)
    nombre_usu = models.CharField(max_length=50, blank=True, null=True)
    apellido_usu = models.CharField(max_length=30, blank=True, null=True)
    fk_id_prf = models.ForeignKey(profile, models.DO_NOTHING, db_column='fk_id_prf', blank=True, null=True)
    estado_usu = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id_usu:
            self.password_usu = make_password(self.password_usu)
        super(users, self).save(*args, **kwargs)
    class Meta:
        managed = False
        db_table = 'public\".\"usuario'
