from django.db import models
from apps.bonding.src.models.typeVin import TypeVin
from apps.bonding.src.models.tutorVin import TutorVin
from apps.bonding.src.models.projectVin import Projectvin

class Process(models.Model):
    id_prov = models.AutoField(primary_key=True)
    nombre_prov = models.CharField(max_length=250)
    descripcion_prov = models.TextField()
    estado_prov = models.CharField(max_length=15)
    fecha_creacion_prov = models.DateTimeField()
    fecha_actualizacion_prov = models.DateTimeField()
    usuario_creacion_prov = models.CharField(max_length=250)
    usuario_actualizacion_prov = models.CharField(max_length=250)
    fk_id_proy = models.ForeignKey(Projectvin, models.DO_NOTHING, db_column='fk_id_proy', blank=True, null=True)
    fk_id_tipo = models.ForeignKey(TypeVin, models.DO_NOTHING, db_column='fk_id_tipo', blank=True, null=True)
    fk_id_doc = models.IntegerField(blank=True, null=True)
    fk_id_per = models.IntegerField(blank=True, null=True)
    fk_id_car = models.IntegerField(blank=True, null=True)
    fk_id_cur = models.IntegerField(blank=True, null=True)
    fk_id_tut = models.ForeignKey(TutorVin, models.DO_NOTHING, db_column='fk_id_tut', blank=True, null=True)

    class Meta:
        db_table = 'vinculacion\".\"procesovinculacion'