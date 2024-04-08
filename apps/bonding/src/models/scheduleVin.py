from django.db import models

class ScheduleVin(models.Model):
    id_cro = models.AutoField(primary_key=True)
    semanauno_cro = models.TextField()
    semanados_cro = models.TextField()
    semanatres_cro = models.TextField()
    semanacuatro_cro = models.TextField()
    semanacinco_cro = models.TextField()
    semanaseis_cro = models.TextField()
    semanasiete_cro = models.TextField()
    semanaocho_cro = models.TextField()
    semananueve_cro = models.TextField()
    semanadiez_cro = models.TextField()
    semanaonce_cro = models.TextField()
    semanadose_cro = models.TextField()
    semanatrese_cro = models.TextField()
    semanacatorse_cro = models.TextField()
    semanaquinse_cro = models.TextField()
    semanadiecises_cro = models.TextField()
    estado_cro = models.CharField(db_column='estado__cro', max_length=15)  # Field renamed because it contained more than one '_' in a row.
    fecha_creacion_cro = models.DateTimeField()
    fecha_actualizacion_cro = models.DateTimeField()
    usuario_creacion_cro = models.CharField(max_length=250)
    usuario_actualizacion_cro = models.CharField(max_length=250)
    fk_id_prf = models.IntegerField(blank=True, null=True)
    fk_id_per = models.IntegerField(blank=True, null=True)
    fk_id_car = models.IntegerField(blank=True, null=True)
    fk_id_est = models.IntegerField(blank=True, null=True)
    fk_id_doc = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'vinculacion\".\"cronogramavin'