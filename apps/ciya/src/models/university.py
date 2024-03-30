from django.db import models
from .base import BaseModel

class universidad(BaseModel):
    id_uni = models.AutoField(primary_key=True)
    nombre_uni = models.TextField()
    direccion_uni = models.CharField(max_length=40, null=True, blank=True)
    ruc_uni = models.CharField(max_length=40)
    telefono_uni = models.CharField(max_length=40)
    mision_uni = models.TextField()
    vision_uni = models.TextField()
    email_uni = models.CharField(max_length=40, null=True, blank=True)
    facebook_uni = models.CharField(max_length=40)
    twitter_uni = models.CharField(max_length=40)
    instagram_uni = models.CharField(max_length=40)
    pagina_web_uni = models.CharField(max_length=30)
    sede_uni = models.CharField(max_length=50)
    logo_uni = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'universidad'