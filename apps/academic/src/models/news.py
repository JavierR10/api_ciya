from django.db import models


class News(models.Model):
    id_not = models.AutoField(primary_key=True)
    titulo_not = models.CharField(max_length=100, blank=True, null=True)
    descripcion_not = models.TextField(blank=True, null=True)
    imagen_not = models.CharField(max_length=100, blank=True, null=True)
    estado_not = models.CharField(max_length=20, blank=True, null=True)
    fecha_creacion_not = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'academico\".\"noticia'

