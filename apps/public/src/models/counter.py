from django.db import models


class Counter(models.Model):
    id_con = models.AutoField(primary_key=True)
    fecha_con = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'public\".\"contador'
