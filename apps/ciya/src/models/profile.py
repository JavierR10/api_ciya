from django.db import models
from django.utils import timezone
from .base import BaseModel

class profile(BaseModel):
    id_prf = models.AutoField(primary_key=True)
    nombre_prf = models.CharField(max_length=40)
    descripcion_prf = models.TextField()
    
    def delete(self):
        self.deleted_at = timezone.now()  # Establecer la fecha de eliminación
        self.save()

    class Meta:
        db_table = 'perfil'
    
