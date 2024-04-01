# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AreaCarrera(models.Model):
    id_area_car = models.AutoField(primary_key=True)
    nombre_area_car = models.CharField(max_length=250, blank=True, null=True)
    descripcion_area_car = models.TextField(blank=True, null=True)
    foto_area_car = models.CharField(max_length=1500, blank=True, null=True)
    fk_id_car = models.ForeignKey('Carrera', models.DO_NOTHING, db_column='fk_id_car', blank=True, null=True)
    fk_id_doc = models.ForeignKey('Docente', models.DO_NOTHING, db_column='fk_id_doc', blank=True, null=True)

    class Meta:

        db_table = 'area_carrera'


class BancoTemas(models.Model):
    id_ban = models.AutoField(primary_key=True)
    fk_id_doc = models.IntegerField(blank=True, null=True)
    fk_id_lin = models.ForeignKey('Linea', models.DO_NOTHING, db_column='fk_id_lin', blank=True, null=True)
    fk_id_sub = models.IntegerField(blank=True, null=True)
    tema_ban = models.CharField(max_length=500, blank=True, null=True)
    descripcion_ban = models.TextField(blank=True, null=True)
    archivo_adjunto_ban = models.CharField(max_length=1500, blank=True, null=True)
    fecha_creacion_ban = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_ban = models.DateTimeField(blank=True, null=True)
    usuario_creacion_ban = models.CharField(max_length=255, blank=True, null=True)
    usuario_actualizacion_ban = models.CharField(max_length=255, blank=True, null=True)
    validacion_ban = models.CharField(max_length=100, blank=True, null=True)
    estado_ban = models.CharField(max_length=50, blank=True, null=True)

    class Meta:

        db_table = 'banco_temas'


class Carpeta(models.Model):
    id_carp = models.AutoField(primary_key=True)
    parend_id_carp = models.IntegerField(blank=True, null=True)
    nombre_carp = models.CharField(max_length=100, blank=True, null=True)
    fk_id_usu = models.IntegerField(blank=True, null=True)
    descripcion_carp = models.CharField(max_length=200, blank=True, null=True)
    fecha_cierre_carp = models.DateField(blank=True, null=True)
    hora_cierre_carp = models.TimeField(blank=True, null=True)
    estado_carp = models.CharField(max_length=20, blank=True, null=True)
    disposicion_carp = models.CharField(max_length=20, blank=True, null=True)
    fecha_creacion_carp = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_carp = models.DateTimeField(blank=True, null=True)

    class Meta:

        db_table = 'carpeta'


class Comicionado(models.Model):
    id_comi = models.AutoField(primary_key=True)
    estado_comi = models.CharField(max_length=15)
    fecha_creacion_comi = models.DateTimeField()
    fecha_actualizacion_comi = models.DateTimeField()
    usuario_creacion_comi = models.CharField(max_length=250)
    usuario_actualizacion_comi = models.CharField(max_length=250)
    fk_id_doc = models.IntegerField(blank=True, null=True)
    fk_id_per = models.IntegerField(blank=True, null=True)
    fk_id_car = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'comicionado'


class Comicionadovin(models.Model):
    id_comi = models.AutoField(primary_key=True)
    estado_comi = models.CharField(max_length=15)
    fecha_creacion_comi = models.DateTimeField()
    fecha_actualizacion_comi = models.DateTimeField()
    usuario_creacion_comi = models.CharField(max_length=250)
    usuario_actualizacion_comi = models.CharField(max_length=250)
    fk_id_doc = models.IntegerField(blank=True, null=True)
    fk_id_per = models.IntegerField(blank=True, null=True)
    fk_id_car = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'comicionadovin'


class Contador(models.Model):
    id_con = models.AutoField(primary_key=True)
    fecha_con = models.DateTimeField(blank=True, null=True)

    class Meta:

        db_table = 'contador'


class Convenio(models.Model):
    id_con = models.AutoField(primary_key=True)
    documento_con = models.CharField(max_length=1500, blank=True, null=True)
    fecha_inicio_con = models.DateField(blank=True, null=True)
    fecha_fin_con = models.DateField(blank=True, null=True)
    fk_id_emp = models.IntegerField()
    fecha_creacion_con = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_con = models.DateTimeField(blank=True, null=True)
    usuario_creacion_con = models.CharField(max_length=255, blank=True, null=True)
    usuario_actualizacion_con = models.CharField(max_length=255, blank=True, null=True)
    tipo_con = models.CharField(max_length=50, blank=True, null=True)
    estado_con = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'convenio'


class ConvenioCarrera(models.Model):
    id_con_car = models.AutoField(primary_key=True)
    fk_id_con = models.ForeignKey(Convenio, models.DO_NOTHING, db_column='fk_id_con', blank=True, null=True)
    fk_id_car = models.BigIntegerField(blank=True, null=True)

    class Meta:

        db_table = 'convenio_carrera'





class Cronogramavin(models.Model):
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

        db_table = 'cronogramavin'


class Curso(models.Model):
    id_cur = models.AutoField(primary_key=True)
    fk_id_malla = models.IntegerField(blank=True, null=True)
    nombre_cur = models.CharField(max_length=50, blank=True, null=True)
    fecha_creacion_cur = models.DateField(blank=True, null=True)
    fecha_actualizacion_cur = models.DateField(blank=True, null=True)
    usuario_creacion_cur = models.CharField(max_length=100, blank=True, null=True)
    usuario_actualizacion_cur = models.CharField(max_length=100, blank=True, null=True)

    class Meta:

        db_table = 'curso'


class Distributivo(models.Model):
    id_dis = models.AutoField(primary_key=True)
    fk_id_per = models.IntegerField(blank=True, null=True)
    fk_id_mat = models.IntegerField(blank=True, null=True)
    fk_id_doc = models.IntegerField(blank=True, null=True)
    paralelo_dis = models.CharField(max_length=2, blank=True, null=True)
    silabo_dis = models.CharField(max_length=200, blank=True, null=True)
    fecha_creacion_dis = models.DateField(blank=True, null=True)
    fecha_actualizacion_dis = models.DateField(blank=True, null=True)
    usuario = models.CharField(max_length=100, blank=True, null=True)

    class Meta:

        db_table = 'distributivo'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:

        db_table = 'django_migrations'



class Documentovin(models.Model):
    id_doc = models.AutoField(primary_key=True)
    nombre_doc = models.CharField(max_length=250)
    descripcion_doc = models.CharField(max_length=250)
    estado_doc = models.CharField(max_length=15)
    fecha_creacion_doc = models.DateTimeField()
    fecha_actualizacion_doc = models.DateTimeField()
    usuario_creacion_doc = models.CharField(max_length=250)
    usuario_actualizacion_doc = models.CharField(max_length=250)
    documento_doc = models.CharField(max_length=250)
    fk_id_proy = models.ForeignKey('Proyectovin', models.DO_NOTHING, db_column='fk_id_proy', blank=True, null=True)

    class Meta:

        db_table = 'documentovin'


class Empresa(models.Model):
    id_emp = models.AutoField(primary_key=True)
    ruc_emp = models.CharField(max_length=15, blank=True, null=True)
    nombre_emp = models.CharField(max_length=500, blank=True, null=True)
    provincia_emp = models.CharField(max_length=100, blank=True, null=True)
    canton_emp = models.CharField(max_length=100, blank=True, null=True)
    direccion_emp = models.CharField(max_length=500, blank=True, null=True)
    latitud_emp = models.FloatField(blank=True, null=True)
    longitud_emp = models.FloatField(blank=True, null=True)
    telefono_emp = models.CharField(max_length=150, blank=True, null=True)
    correo_emp = models.CharField(max_length=150, blank=True, null=True)
    logo_emp = models.CharField(max_length=450, blank=True, null=True)
    tipo_emp = models.CharField(max_length=500, blank=True, null=True)
    estado_emp = models.CharField(max_length=50, blank=True, null=True)
    fecha_creacion_emp = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_emp = models.DateTimeField(blank=True, null=True)
    usuario_creacion_emp = models.CharField(max_length=255, blank=True, null=True)
    usuario_actualizacion_emp = models.CharField(max_length=255, blank=True, null=True)
    parroquia_emp = models.CharField(max_length=2500, blank=True, null=True)
    actividad_emp = models.TextField(blank=True, null=True)
    sector_economico_emp = models.TextField(blank=True, null=True)

    class Meta:

        db_table = 'empresa'


class Estudiantes(models.Model):
    id_est = models.AutoField(primary_key=True)
    cedula_est = models.CharField(max_length=100, blank=True, null=True)
    primer_apellido_est = models.CharField(max_length=100, blank=True, null=True)
    segundo_apellido_est = models.CharField(max_length=100, blank=True, null=True)
    nombre_est = models.CharField(max_length=100, blank=True, null=True)
    email_est = models.CharField(max_length=100, blank=True, null=True)
    telefono_est = models.CharField(max_length=100, blank=True, null=True)
    ciclo_est = models.CharField(max_length=100, blank=True, null=True)
    fk_id_fac = models.ForeignKey('Facultad', models.DO_NOTHING, db_column='fk_id_fac', blank=True, null=True)
    fk_id_car = models.ForeignKey(Carrera, models.DO_NOTHING, db_column='fk_id_car', blank=True, null=True)
    celular_est = models.CharField(max_length=100, blank=True, null=True)
    genero_est = models.CharField(max_length=100, blank=True, null=True)
    estado_civil_est = models.CharField(max_length=100, blank=True, null=True)
    etnia_est = models.CharField(max_length=100, blank=True, null=True)
    discapacidad_est = models.CharField(max_length=100, blank=True, null=True)
    provincia_est = models.CharField(max_length=150, blank=True, null=True)
    ciudad_est = models.CharField(max_length=150, blank=True, null=True)
    parroquia_est = models.CharField(max_length=500, blank=True, null=True)
    direccion_est = models.CharField(max_length=500, blank=True, null=True)
    fk_id_per = models.ForeignKey('Periodo', models.DO_NOTHING, db_column='fk_id_per', blank=True, null=True)
    fk_id_usu = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'estudiantes'


class Facultad(models.Model):
    id_fac = models.AutoField(primary_key=True)
    nombre_fac = models.CharField(max_length=100, blank=True, null=True)
    siglas_fac = models.CharField(max_length=10, blank=True, null=True)
    fk_decano_fac = models.IntegerField(blank=True, null=True)
    fk_vicedecano_fac = models.IntegerField(blank=True, null=True)
    correo_fac = models.CharField(max_length=50, blank=True, null=True)
    telefono_fac = models.CharField(max_length=10, blank=True, null=True)
    fecha_creacion_fac = models.DateField(blank=True, null=True)
    fecha_actualizacion_fac = models.DateField(blank=True, null=True)
    usuario_creacion_fac = models.CharField(max_length=100, blank=True, null=True)
    usuario_actualizacion_fac = models.CharField(max_length=100, blank=True, null=True)
    mision_fac = models.CharField(max_length=500, blank=True, null=True)
    vision_fac = models.CharField(max_length=500, blank=True, null=True)
    logo_fac = models.CharField(max_length=1500, blank=True, null=True)

    class Meta:

        db_table = 'facultad'


class Grupovin(models.Model):
    id_grupo = models.AutoField(primary_key=True)
    nombre_grupo = models.CharField(max_length=250)
    numero_grupo = models.TextField()
    estado_grupo = models.CharField(max_length=15)
    fecha_creacion_grupo = models.DateTimeField()
    fecha_actualizacion_grupo = models.DateTimeField()
    usuario_creacion_grupo = models.CharField(max_length=250)
    usuario_actualizacion_grupo = models.CharField(max_length=250)
    fk_id_prov = models.ForeignKey('Procesovinculacion', models.DO_NOTHING, db_column='fk_id_prov', blank=True, null=True)
    fk_id_con = models.ForeignKey(Convenio, models.DO_NOTHING, db_column='fk_id_con', blank=True, null=True)
    fk_id_cur = models.IntegerField(blank=True, null=True)
    fk_id_emp = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='fk_id_emp', blank=True, null=True)

    class Meta:

        db_table = 'grupovin'



class HorarioIndividual(models.Model):
    id_horaindi = models.AutoField(primary_key=True)
    archivo_horaindi = models.CharField(max_length=255, blank=True, null=True)
    fk_id_doc = models.IntegerField(blank=True, null=True)
    fk_id_per = models.IntegerField(blank=True, null=True)
    fecha_creacion_horaindi = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_horaindi = models.DateTimeField(blank=True, null=True)
    usuario_creacion_horaindi = models.CharField(max_length=100, blank=True, null=True)
    usuario_actualizacion_horaindi = models.CharField(max_length=100, blank=True, null=True)

    class Meta:

        db_table = 'horario_individual'


class Integrantevin(models.Model):
    id_inte = models.AutoField(primary_key=True)
    estado_inte = models.CharField(max_length=15)
    fecha_creacion_inte = models.DateTimeField()
    fecha_actualizacion_inte = models.DateTimeField()
    usuario_creacion_inte = models.CharField(max_length=250)
    usuario_actualizacion_inte = models.CharField(max_length=250)
    fk_id_grupo = models.ForeignKey(Grupovin, models.DO_NOTHING, db_column='fk_id_grupo', blank=True, null=True)
    fk_id_matr = models.ForeignKey('Matriculavin', models.DO_NOTHING, db_column='fk_id_matr', blank=True, null=True)

    class Meta:

        db_table = 'integrantevin'



class MallaAcademica(models.Model):
    id_malla = models.AutoField(primary_key=True)
    fk_id_car = models.IntegerField(blank=True, null=True)
    nombre_malla = models.CharField(max_length=255, blank=True, null=True)
    descripcion_malla = models.CharField(max_length=255, blank=True, null=True)
    estado_malla = models.CharField(max_length=25, blank=True, null=True)
    archivo_malla = models.CharField(max_length=255, blank=True, null=True)
    fecha_creacion_malla = models.DateField(blank=True, null=True)
    fecha_actualizacion_malla = models.DateField(blank=True, null=True)
    usuario_creacion_malla = models.CharField(max_length=255, blank=True, null=True)
    usuario_actualizacion_malla = models.CharField(max_length=255, blank=True, null=True)

    class Meta:

        db_table = 'malla_academica'


class Materia(models.Model):
    id_mat = models.AutoField(primary_key=True)
    fk_id_cur = models.IntegerField(blank=True, null=True)
    nombre_mat = models.CharField(max_length=200, blank=True, null=True)
    descripcion_mat = models.CharField(max_length=900, blank=True, null=True)
    fecha_creacion_mat = models.DateField(blank=True, null=True)
    fecha_actualizacion_mat = models.DateField(blank=True, null=True)
    usuario_creacion_mat = models.CharField(max_length=100, blank=True, null=True)
    usuario_actualizacion_mat = models.CharField(max_length=100, blank=True, null=True)
    fk_id_car = models.ForeignKey(Carrera, models.DO_NOTHING, db_column='fk_id_car', blank=True, null=True)
    fk_id_malla = models.ForeignKey(MallaAcademica, models.DO_NOTHING, db_column='fk_id_malla', blank=True, null=True)
    codigo_mat = models.CharField(max_length=15, blank=True, null=True)
    fk_id_doc = models.ForeignKey(Docente, models.DO_NOTHING, db_column='fk_id_doc', blank=True, null=True)
    tipo_mat = models.CharField(max_length=200, blank=True, null=True)

    class Meta:

        db_table = 'materia'


class Matriculavin(models.Model):
    id_matr = models.AutoField(primary_key=True)
    estado_matr = models.CharField(max_length=15)
    fecha_creacion_matr = models.DateTimeField()
    fecha_actualizacion_matr = models.DateTimeField()
    usuario_creacion_matr = models.CharField(max_length=250)
    usuario_actualizacion_matr = models.CharField(max_length=250)
    fk_id_est = models.IntegerField(blank=True, null=True)
    fk_id_per = models.IntegerField(blank=True, null=True)
    fk_id_tipo = models.ForeignKey('Tipovin', models.DO_NOTHING, db_column='fk_id_tipo', blank=True, null=True)
    fk_id_car = models.IntegerField(blank=True, null=True)
    fk_id_cur = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'matriculavin'


class Modulos(models.Model):
    id_mod = models.AutoField(primary_key=True)
    nombre_mod = models.CharField(max_length=150, blank=True, null=True)
    descripcion_mod = models.CharField(max_length=400, blank=True, null=True)

    class Meta:

        db_table = 'modulos'


class Periodo(models.Model):
    id_per = models.AutoField(primary_key=True)
    fecha_inicio_per = models.DateField(blank=True, null=True)
    fecha_cierre_per = models.DateField(blank=True, null=True)
    rango_per = models.CharField(max_length=255)
    fecha_creacion_per = models.DateField(blank=True, null=True)
    fecha_actualizacion_per = models.DateField(blank=True, null=True)
    estado_per = models.CharField(max_length=25, blank=True, null=True)
    usuario_creacion_per = models.CharField(max_length=255, blank=True, null=True)
    usuario_actualizacion_per = models.CharField(max_length=255, blank=True, null=True)

    class Meta:

        db_table = 'periodo'


class Permisos(models.Model):
    id_prm = models.AutoField(primary_key=True)
    fk_id_seg = models.ForeignKey('Seguridad', models.DO_NOTHING, db_column='fk_id_seg', blank=True, null=True)
    fk_id_prf = models.ForeignKey(Perfil, models.DO_NOTHING, db_column='fk_id_prf', blank=True, null=True)
    permiso_visualizar_prm = models.SmallIntegerField(blank=True, null=True)
    permiso_agregar = models.SmallIntegerField(blank=True, null=True)
    permiso_editar = models.SmallIntegerField(blank=True, null=True)
    permiso_eliminar = models.SmallIntegerField(blank=True, null=True)
    permiso_imprimir = models.SmallIntegerField(blank=True, null=True)

    class Meta:

        db_table = 'permisos'


class Proceso(models.Model):
    id_proc = models.AutoField(primary_key=True)
    fk_id_per = models.IntegerField(blank=True, null=True)
    fk_id_tip = models.ForeignKey('Tipo', models.DO_NOTHING, db_column='fk_id_tip', blank=True, null=True)
    fk_id_con = models.IntegerField(blank=True, null=True)
    fk_id_doc = models.IntegerField(blank=True, null=True)
    tema_proc = models.TextField(blank=True, null=True)
    fecha_creacion_proc = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_proc = models.DateTimeField(blank=True, null=True)
    usuario_creacion_proc = models.CharField(max_length=255, blank=True, null=True)
    usuario_actualizacion_proc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:

        db_table = 'proceso'


class Procesovinculacion(models.Model):
    id_prov = models.AutoField(primary_key=True)
    nombre_prov = models.CharField(max_length=250)
    descripcion_prov = models.TextField()
    estado_prov = models.CharField(max_length=15)
    fecha_creacion_prov = models.DateTimeField()
    fecha_actualizacion_prov = models.DateTimeField()
    usuario_creacion_prov = models.CharField(max_length=250)
    usuario_actualizacion_prov = models.CharField(max_length=250)
    fk_id_proy = models.ForeignKey('Proyectovin', models.DO_NOTHING, db_column='fk_id_proy', blank=True, null=True)
    fk_id_tipo = models.ForeignKey('Tipovin', models.DO_NOTHING, db_column='fk_id_tipo', blank=True, null=True)
    fk_id_doc = models.IntegerField(blank=True, null=True)
    fk_id_per = models.IntegerField(blank=True, null=True)
    fk_id_car = models.IntegerField(blank=True, null=True)
    fk_id_cur = models.IntegerField(blank=True, null=True)
    fk_id_tut = models.ForeignKey('Tutorvin', models.DO_NOTHING, db_column='fk_id_tut', blank=True, null=True)

    class Meta:

        db_table = 'procesovinculacion'


class Programavin(models.Model):
    id_prog = models.AutoField(primary_key=True)
    nombre_prog = models.CharField(max_length=250)
    descripcion_prog = models.TextField()
    estado_prog = models.CharField(max_length=15)
    fecha_creacion_prog = models.DateTimeField()
    fecha_actualizacion_prog = models.DateTimeField()
    usuario_creacion_prog = models.CharField(max_length=250)
    usuario_actualizacion_prog = models.CharField(max_length=250)
    fk_id_fac = models.IntegerField(blank=True, null=True)
    archivo_prog = models.CharField(max_length=1500, blank=True, null=True)

    class Meta:

        db_table = 'programavin'


class Proyectovin(models.Model):
    id_proy = models.AutoField(primary_key=True)
    nombre_proy = models.CharField(max_length=250)
    descripcion_proy = models.TextField()
    estado_proy = models.CharField(max_length=15)
    fecha_creacion_proy = models.DateTimeField()
    fecha_actualizacion_proy = models.DateTimeField()
    usuario_creacion_proy = models.CharField(max_length=250)
    usuario_actualizacion_proy = models.CharField(max_length=250)
    fk_id_car = models.IntegerField(blank=True, null=True)
    fk_id_per = models.IntegerField(blank=True, null=True)
    fk_id_prog = models.ForeignKey(Programavin, models.DO_NOTHING, db_column='fk_id_prog', blank=True, null=True)

    class Meta:

        db_table = 'proyectovin'


class RepresentantesEstudiantiles(models.Model):
    id_repest = models.AutoField(primary_key=True)
    primer_apellido_repest = models.CharField(max_length=100, blank=True, null=True)
    segundo_apellido_repest = models.CharField(max_length=100, blank=True, null=True)
    nombre_repest = models.CharField(max_length=100, blank=True, null=True)
    correo_repest = models.CharField(max_length=100, blank=True, null=True)
    telefono_repest = models.CharField(max_length=100, blank=True, null=True)
    fk_id_car = models.ForeignKey(Carrera, models.DO_NOTHING, db_column='fk_id_car', blank=True, null=True)
    foto_repest = models.CharField(max_length=500, blank=True, null=True)

    class Meta:

        db_table = 'representantes_estudiantiles'

class Seguridad(models.Model):
    id_seg = models.AutoField(primary_key=True)
    fk_id_mod = models.ForeignKey(Modulos, models.DO_NOTHING, db_column='fk_id_mod', blank=True, null=True)
    nombre_seg = models.CharField(max_length=150, blank=True, null=True)
    descripcion_seg = models.CharField(max_length=500, blank=True, null=True)

    class Meta:

        db_table = 'seguridad'


class Tipo(models.Model):
    id_tip = models.AutoField(primary_key=True)
    nombre_tip = models.TextField(blank=True, null=True)
    siglas_tip = models.CharField(max_length=50, blank=True, null=True)
    estado_tip = models.IntegerField(blank=True, null=True)
    fecha_creacion_tip = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_tip = models.DateTimeField(blank=True, null=True)
    usuario_creacion_tip = models.CharField(max_length=255, blank=True, null=True)
    usuario_actualizacion_tip = models.CharField(max_length=255, blank=True, null=True)

    class Meta:

        db_table = 'tipo'




class Tipovin(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    nombre_tipo = models.CharField(max_length=250)
    siglas_tipo = models.CharField(max_length=250)
    descripcion_tipo = models.TextField()
    estado_tipo = models.CharField(max_length=15)
    fecha_creacion_tipo = models.DateTimeField()
    fecha_actualizacion_tipo = models.DateTimeField()
    usuario_creacion_tipo = models.CharField(max_length=250)
    usuario_actualizacion_tipo = models.CharField(max_length=250)

    class Meta:

        db_table = 'tipovin'


class Tutorvin(models.Model):
    id_tut = models.AutoField(primary_key=True)
    estado_tut = models.CharField(max_length=15)
    fecha_creacion_tut = models.DateTimeField()
    fecha_actualizacion_tut = models.DateTimeField()
    usuario_creacion_tut = models.CharField(max_length=250)
    usuario_actualizacion_tut = models.CharField(max_length=250)
    fk_id_doc = models.IntegerField(blank=True, null=True)
    fk_id_per = models.IntegerField(blank=True, null=True)
    fk_id_tipo = models.ForeignKey(Tipovin, models.DO_NOTHING, db_column='fk_id_tipo', blank=True, null=True)
    fk_id_car = models.IntegerField(blank=True, null=True)
    fk_id_cur = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'tutorvin'


