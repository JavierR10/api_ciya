from django.db import models
from django.utils import timezone
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
        db_table = 'universidad'