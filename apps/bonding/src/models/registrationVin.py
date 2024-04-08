from django.db import models
from apps.bonding.src.models.typeVin import TypeVin

class RegistrationVin(models.Model):
    id_matr = models.AutoField(primary_key=True)
    estado_matr = models.CharField(max_length=15)
    fecha_creacion_matr = models.DateTimeField()
    fecha_actualizacion_matr = models.DateTimeField()
    usuario_creacion_matr = models.CharField(max_length=250)
    usuario_actualizacion_matr = models.CharField(max_length=250)
    fk_id_est = models.IntegerField(blank=True, null=True)
    fk_id_per = models.IntegerField(blank=True, null=True)
    fk_id_tipo = models.ForeignKey(TypeVin, models.DO_NOTHING, db_column='fk_id_tipo', blank=True, null=True)
    fk_id_car = models.IntegerField(blank=True, null=True)
    fk_id_cur = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'vinculacion\".\"matriculavin'