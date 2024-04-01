from django.db import models
class ProjectType(models.Model):
    id_tip = models.AutoField(primary_key=True)
    nombre_tip = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'investigacion\".\"tipo_proyecto'

