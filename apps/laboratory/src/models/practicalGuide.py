from django.db import models

class PracticalGuide(models.Model):
    id_guia = models.AutoField(primary_key=True)
    numero_practica_guia = models.CharField(max_length=255, blank=True, null=True)
    tema_guia = models.CharField(max_length=255, blank=True, null=True)
    fecha_inicial_guia = models.DateField(blank=True, null=True)
    fecha_final_guia = models.DateField(blank=True, null=True)
    archivo_guia = models.CharField(max_length=255, blank=True, null=True)
    fk_id_doc = models.BigIntegerField(blank=True, null=True)
    objetivo_guia = models.TextField(blank=True, null=True)
    instrucciones_guia = models.TextField(blank=True, null=True)
    resultados_esperados_guia = models.TextField(blank=True, null=True)
    bibliografia_guia = models.TextField(blank=True, null=True)
    fk_id_lab = models.BigIntegerField(blank=True, null=True)
    fecha_creacion_guia = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_guia = models.DateTimeField(blank=True, null=True)
    usuario_creacion_guia = models.CharField(max_length=255, blank=True, null=True)
    usuario_actualizacion_guia = models.CharField(max_length=255, blank=True, null=True)
    fk_id_per = models.BigIntegerField(blank=True, null=True)
    fk_id_cur = models.BigIntegerField(blank=True, null=True)
    fk_id_mat = models.BigIntegerField(blank=True, null=True)
    fk_id_malla = models.BigIntegerField(blank=True, null=True)
    area_guia = models.TextField(blank=True, null=True)
    medidas_guia = models.TextField(blank=True, null=True)
    instrumentos_guia = models.TextField(blank=True, null=True)
    trabajopreparatorio_guia = models.TextField(blank=True, null=True)
    actividades_guia = models.TextField(blank=True, null=True)
    informacion_guia = models.TextField(blank=True, null=True)
    fk_laboratorista_aprobado = models.BigIntegerField(blank=True, null=True)
    fk_director_aprobado = models.BigIntegerField(blank=True, null=True)
    fecha_laboratorista_aprobado = models.DateTimeField(blank=True, null=True)
    fecha_director_aprobado = models.DateTimeField(blank=True, null=True)
    hora_guia = models.IntegerField(blank=True, null=True)
    fk_id_lin = models.IntegerField(blank=True, null=True)
    fk_id_sub = models.IntegerField(blank=True, null=True)
    fk_id_coordinador_id_doc = models.CharField(max_length=250, blank=True, null=True)
    fk_id_car = models.IntegerField(blank=True, null=True)
    paralelo_guia = models.CharField(max_length=5, blank=True, null=True)
    metodologia_guia = models.TextField(blank=True, null=True)
    estado_guia_practica = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'laboratorios\".\"guiapractica'

