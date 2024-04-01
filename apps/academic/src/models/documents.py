from django.db import models

class Documents(models.Model):
    id_doc = models.AutoField(primary_key=True)
    fk_id_carp = models.IntegerField(blank=True, null=True)
    nombre_doc = models.CharField(max_length=100, blank=True, null=True)
    documento_doc = models.CharField(max_length=100, blank=True, null=True)
    descripcion_doc = models.CharField(max_length=200, blank=True, null=True)
    fecha_entrega_doc = models.DateField(blank=True, null=True)
    fecha_creacion_doc = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_doc = models.DateTimeField(blank=True, null=True)
    usuario_creacion_doc = models.CharField(max_length=255, blank=True, null=True)
    usuario_actualizacion_doc = models.CharField(max_length=255, blank=True, null=True)
    fk_id_usu = models.IntegerField(blank=True, null=True)
    publico_doc = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'academico\".\"documento'

