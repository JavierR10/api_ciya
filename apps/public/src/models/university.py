from django.db import models


class universidad(models.Model):
    id_uni = models.AutoField(primary_key=True)
    nombre_uni = models.CharField(max_length=50, blank=True, null=True)
    direccion_uni = models.CharField(max_length=100, blank=True, null=True)
    ruc_uni = models.CharField(max_length=15, blank=True, null=True)
    telefono_uni = models.CharField(max_length=15, blank=True, null=True)
    mision_uni = models.CharField(max_length=500, blank=True, null=True)
    vision_uni = models.CharField(max_length=500, blank=True, null=True)
    email_uni = models.CharField(max_length=30, blank=True, null=True)
    facebook_uni = models.CharField(max_length=40, blank=True, null=True)
    twitter_uni = models.CharField(max_length=40, blank=True, null=True)
    instagram_uni = models.CharField(max_length=40, blank=True, null=True)
    pagina_web_uni = models.CharField(max_length=30, blank=True, null=True)
    sede_uni = models.CharField(max_length=50, blank=True, null=True)
    logo_uni = models.CharField(max_length=255, blank=True, null=True)
    fecha_creacion_car = models.DateField(blank=True, null=True)
    fecha_actualizacion_car = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'public\".\"universidad'
