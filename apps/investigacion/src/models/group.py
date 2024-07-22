from django.db import models

class Group(models.Model):
    id_gru = models.AutoField(primary_key=True)
    nombre_gru = models.CharField(max_length=200, blank=True, null=True)
    tipo_gru = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'investigacion\".\"grupo'

