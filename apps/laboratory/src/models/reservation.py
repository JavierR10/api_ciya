from django.db import models


class Reservation(models.Model):
    id_res = models.AutoField(primary_key=True)
    fk_id_tipres = models.IntegerField(blank=True, null=True)
    fk_id_doc = models.IntegerField(blank=True, null=True)
    fk_id_lab = models.IntegerField(blank=True, null=True)
    fk_id_area = models.IntegerField(blank=True, null=True)
    fk_id_guia = models.IntegerField(blank=True, null=True)
    tema_res = models.TextField(blank=True, null=True)
    comentario_res = models.TextField(blank=True, null=True)
    estado_res = models.CharField(max_length=100, blank=True, null=True)
    fecha_hora_res = models.DateTimeField(blank=True, null=True)
    duracion_res = models.IntegerField(blank=True, null=True)
    numero_participantes_res = models.IntegerField(blank=True, null=True)
    descripcion_participantes_res = models.TextField(blank=True, null=True)
    materiales_res = models.TextField(blank=True, null=True)
    fecha_creacion_res = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_res = models.DateTimeField(blank=True, null=True)
    usuario_creacion_res = models.CharField(max_length=255, blank=True, null=True)
    usuario_actualizacion_res = models.CharField(max_length=255, blank=True, null=True)
    fecha_hora_fin_res = models.DateTimeField(blank=True, null=True)
    observaciones_finales_res = models.TextField(blank=True, null=True)
    asistencia_res = models.CharField(max_length=50, blank=True, null=True)
    guia_adjunta_res = models.CharField(max_length=500, blank=True, null=True)
    curso_res = models.CharField(max_length=150, blank=True, null=True)
    materia_res = models.CharField(max_length=150, blank=True, null=True)
    fk_id_car = models.IntegerField(blank=True, null=True)
    paralelo_res = models.CharField(max_length=150, blank=True, null=True)
    tipo_texto_res = models.CharField(max_length=150, blank=True, null=True)
    fk_id_usu = models.IntegerField(blank=True, null=True)
    software_res = models.CharField(max_length=250, blank=True, null=True)
    tipo_res = models.CharField(max_length=20, blank=True, null=True)
    pedidodocente_res = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'laboratorios\".\"reserva'

