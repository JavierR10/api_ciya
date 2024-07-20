from django.db import models
from apps.bonding.src.models.groupVin import GroupVin
from apps.bonding.src.models.registrationVin import RegistrationVin

class IntegranteVin(models.Model):
    id_inte = models.AutoField(primary_key=True)
    estado_inte = models.CharField(max_length=15)
    fecha_creacion_inte = models.DateTimeField()
    fecha_actualizacion_inte = models.DateTimeField()
    usuario_creacion_inte = models.CharField(max_length=250)
    usuario_actualizacion_inte = models.CharField(max_length=250)
    fk_id_grupo = models.ForeignKey(GroupVin, models.DO_NOTHING, db_column='fk_id_grupo', blank=True, null=True)
    fk_id_matr = models.ForeignKey(RegistrationVin, models.DO_NOTHING, db_column='fk_id_matr', blank=True, null=True)

    class Meta:
        db_table = 'vinculacion\".\"integrantevin'