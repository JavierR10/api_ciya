from django.db import models

class Collaborator(models.Model):
    id_col = models.AutoField(primary_key=True)
    fk_id_carp = models.IntegerField(blank=True, null=True)
    fk_id_usu = models.IntegerField(blank=True, null=True)
    entrega_col = models.CharField(max_length=15, blank=True, null=True)
    notificacion_col = models.CharField(max_length=10, blank=True, null=True)
    acceso_col = models.CharField(max_length=10, blank=True, null=True)

    
    class Meta:
        db_table = 'academico\".\"colaborador'

