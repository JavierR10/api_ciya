# Generated by Django 5.0.3 on 2024-04-08 04:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id_area', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_area', models.CharField(blank=True, max_length=500, null=True)),
                ('descripcion_area', models.CharField(blank=True, max_length=2500, null=True)),
                ('imagen_area', models.CharField(blank=True, max_length=1500, null=True)),
                ('fecha_creacion_area', models.DateTimeField(blank=True, null=True)),
                ('fecha_actualizacion_area', models.DateTimeField(blank=True, null=True)),
                ('usuario_creacion_area', models.CharField(blank=True, max_length=255, null=True)),
                ('usuario_actualizacion_area', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'laboratorios"."area',
            },
        ),
        migrations.CreateModel(
            name='AreaLaboratory',
            fields=[
                ('id_labarea', models.AutoField(primary_key=True, serialize=False)),
                ('fk_id_area', models.IntegerField(blank=True, null=True)),
                ('fk_id_lab', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'laboratorios"."laboratorio_area',
            },
        ),
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('id_lab', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_lab', models.CharField(blank=True, max_length=255, null=True)),
                ('descripcion_lab', models.CharField(blank=True, max_length=1000, null=True)),
                ('fotografia1_lab', models.CharField(blank=True, max_length=255, null=True)),
                ('fotografia2_lab', models.CharField(blank=True, max_length=255, null=True)),
                ('fk_docente_responsable_lab', models.IntegerField(blank=True, null=True)),
                ('fk_administrativo_responsable_lab', models.IntegerField(blank=True, null=True)),
                ('fecha_creacion_lab', models.DateTimeField(blank=True, null=True)),
                ('fecha_actualizacion_lab', models.DateTimeField(blank=True, null=True)),
                ('usuario_creacion_lab', models.CharField(blank=True, max_length=255, null=True)),
                ('usuario_actualizacion_lab', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_lab', models.CharField(blank=True, max_length=255, null=True)),
                ('ubicacion_lab', models.CharField(blank=True, max_length=300, null=True)),
                ('color_lab', models.CharField(blank=True, max_length=15, null=True)),
                ('fk_administrativo_responsable_secundario_lab', models.IntegerField(blank=True, null=True)),
                ('siglas_lab', models.CharField(blank=True, max_length=15, null=True)),
                ('paralelo_guia', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'db_table': 'laboratorios"."laboratorio',
            },
        ),
        migrations.CreateModel(
            name='LaboratoryCareer',
            fields=[
                ('id_labcar', models.AutoField(primary_key=True, serialize=False)),
                ('fk_id_lab', models.IntegerField(blank=True, null=True)),
                ('fk_id_car', models.IntegerField(blank=True, null=True)),
                ('fecha_creacion_labcar', models.DateTimeField(blank=True, null=True)),
                ('fecha_actualizacion_labcar', models.DateTimeField(blank=True, null=True)),
                ('usuario_creacion_labcar', models.CharField(blank=True, max_length=255, null=True)),
                ('usuario_actualizacion_labcar', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'laboratorios"."laboratorio_carrera',
            },
        ),
        migrations.CreateModel(
            name='PracticalGuide',
            fields=[
                ('id_guia', models.AutoField(primary_key=True, serialize=False)),
                ('numero_practica_guia', models.CharField(blank=True, max_length=255, null=True)),
                ('tema_guia', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_inicial_guia', models.DateField(blank=True, null=True)),
                ('fecha_final_guia', models.DateField(blank=True, null=True)),
                ('archivo_guia', models.CharField(blank=True, max_length=255, null=True)),
                ('fk_id_doc', models.BigIntegerField(blank=True, null=True)),
                ('objetivo_guia', models.TextField(blank=True, null=True)),
                ('instrucciones_guia', models.TextField(blank=True, null=True)),
                ('resultados_esperados_guia', models.TextField(blank=True, null=True)),
                ('bibliografia_guia', models.TextField(blank=True, null=True)),
                ('fk_id_lab', models.BigIntegerField(blank=True, null=True)),
                ('fecha_creacion_guia', models.DateTimeField(blank=True, null=True)),
                ('fecha_actualizacion_guia', models.DateTimeField(blank=True, null=True)),
                ('usuario_creacion_guia', models.CharField(blank=True, max_length=255, null=True)),
                ('usuario_actualizacion_guia', models.CharField(blank=True, max_length=255, null=True)),
                ('fk_id_per', models.BigIntegerField(blank=True, null=True)),
                ('fk_id_cur', models.BigIntegerField(blank=True, null=True)),
                ('fk_id_mat', models.BigIntegerField(blank=True, null=True)),
                ('fk_id_malla', models.BigIntegerField(blank=True, null=True)),
                ('area_guia', models.TextField(blank=True, null=True)),
                ('medidas_guia', models.TextField(blank=True, null=True)),
                ('instrumentos_guia', models.TextField(blank=True, null=True)),
                ('trabajopreparatorio_guia', models.TextField(blank=True, null=True)),
                ('actividades_guia', models.TextField(blank=True, null=True)),
                ('informacion_guia', models.TextField(blank=True, null=True)),
                ('fk_laboratorista_aprobado', models.BigIntegerField(blank=True, null=True)),
                ('fk_director_aprobado', models.BigIntegerField(blank=True, null=True)),
                ('fecha_laboratorista_aprobado', models.DateTimeField(blank=True, null=True)),
                ('fecha_director_aprobado', models.DateTimeField(blank=True, null=True)),
                ('hora_guia', models.IntegerField(blank=True, null=True)),
                ('fk_id_lin', models.IntegerField(blank=True, null=True)),
                ('fk_id_sub', models.IntegerField(blank=True, null=True)),
                ('fk_id_coordinador_id_doc', models.CharField(blank=True, max_length=250, null=True)),
                ('fk_id_car', models.IntegerField(blank=True, null=True)),
                ('paralelo_guia', models.CharField(blank=True, max_length=5, null=True)),
                ('metodologia_guia', models.TextField(blank=True, null=True)),
                ('estado_guia_practica', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'laboratorios"."guiapractica',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id_res', models.AutoField(primary_key=True, serialize=False)),
                ('fk_id_tipres', models.IntegerField(blank=True, null=True)),
                ('fk_id_doc', models.IntegerField(blank=True, null=True)),
                ('fk_id_lab', models.IntegerField(blank=True, null=True)),
                ('fk_id_area', models.IntegerField(blank=True, null=True)),
                ('fk_id_guia', models.IntegerField(blank=True, null=True)),
                ('tema_res', models.TextField(blank=True, null=True)),
                ('comentario_res', models.TextField(blank=True, null=True)),
                ('estado_res', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_hora_res', models.DateTimeField(blank=True, null=True)),
                ('duracion_res', models.IntegerField(blank=True, null=True)),
                ('numero_participantes_res', models.IntegerField(blank=True, null=True)),
                ('descripcion_participantes_res', models.TextField(blank=True, null=True)),
                ('materiales_res', models.TextField(blank=True, null=True)),
                ('fecha_creacion_res', models.DateTimeField(blank=True, null=True)),
                ('fecha_actualizacion_res', models.DateTimeField(blank=True, null=True)),
                ('usuario_creacion_res', models.CharField(blank=True, max_length=255, null=True)),
                ('usuario_actualizacion_res', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_hora_fin_res', models.DateTimeField(blank=True, null=True)),
                ('observaciones_finales_res', models.TextField(blank=True, null=True)),
                ('asistencia_res', models.CharField(blank=True, max_length=50, null=True)),
                ('guia_adjunta_res', models.CharField(blank=True, max_length=500, null=True)),
                ('curso_res', models.CharField(blank=True, max_length=150, null=True)),
                ('materia_res', models.CharField(blank=True, max_length=150, null=True)),
                ('fk_id_car', models.IntegerField(blank=True, null=True)),
                ('paralelo_res', models.CharField(blank=True, max_length=150, null=True)),
                ('tipo_texto_res', models.CharField(blank=True, max_length=150, null=True)),
                ('fk_id_usu', models.IntegerField(blank=True, null=True)),
                ('software_res', models.CharField(blank=True, max_length=250, null=True)),
                ('tipo_res', models.CharField(blank=True, max_length=20, null=True)),
                ('pedidodocente_res', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'laboratorios"."reserva',
            },
        ),
        migrations.CreateModel(
            name='ReservationType',
            fields=[
                ('id_tipres', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipres', models.CharField(blank=True, max_length=100, null=True)),
                ('estado_tipres', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion_tipres', models.DateTimeField(blank=True, null=True)),
                ('fecha_actualizacion_tipres', models.DateTimeField(blank=True, null=True)),
                ('usuario_creacion_tipres', models.CharField(blank=True, max_length=255, null=True)),
                ('usuario_actualizacion_tipres', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'laboratorios"."tipo_reserva',
            },
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id_sof', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_sof', models.CharField(blank=True, max_length=100, null=True)),
                ('tipolicencia_sof', models.CharField(blank=True, max_length=100, null=True)),
                ('cantidad_sof', models.CharField(blank=True, max_length=100, null=True)),
                ('unidad_sof', models.CharField(blank=True, max_length=50, null=True)),
                ('costounitario_sof', models.CharField(blank=True, max_length=50, null=True)),
                ('costototal_sof', models.CharField(blank=True, max_length=50, null=True)),
                ('aplicaciones_sof', models.CharField(blank=True, max_length=1000, null=True)),
                ('caracteristicas_sof', models.CharField(blank=True, max_length=1000, null=True)),
                ('fecha_creacion_sof', models.DateTimeField(blank=True, null=True)),
                ('fecha_actualizacion_sof', models.DateTimeField(blank=True, null=True)),
                ('usuario_creacion_sof', models.CharField(blank=True, null=True)),
                ('usuario_actualizacion_sof', models.CharField(blank=True, null=True)),
                ('imagen_sof', models.CharField(blank=True, max_length=500, null=True)),
                ('fecha_caducidad_sof', models.CharField(blank=True, max_length=500, null=True)),
                ('enlace_sof', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'laboratorios"."software',
            },
        ),
        migrations.CreateModel(
            name='ObservationGuide',
            fields=[
                ('id_observacion', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_observacion', models.DateTimeField(blank=True, null=True)),
                ('detalle_observacion', models.TextField(blank=True, null=True)),
                ('fk_id_doc', models.IntegerField(blank=True, null=True)),
                ('estado_observaciones_guia_practica', models.CharField(blank=True, max_length=50, null=True)),
                ('fk_id_guia', models.ForeignKey(blank=True, db_column='fk_id_guia', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='laboratory.practicalguide')),
            ],
            options={
                'db_table': 'laboratorios"."observacion_guia',
            },
        ),
        migrations.CreateModel(
            name='HoursExecuted',
            fields=[
                ('id_horeje', models.AutoField(primary_key=True, serialize=False)),
                ('inicio_horeje', models.TimeField(blank=True, null=True)),
                ('fecha_creacion_res', models.DateTimeField(blank=True, null=True)),
                ('fecha_actualizacion_res', models.DateTimeField(blank=True, null=True)),
                ('fk_id_res', models.ForeignKey(blank=True, db_column='fk_id_res', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='laboratory.reservation')),
            ],
            options={
                'db_table': 'laboratorios"."horas_ejecutadas',
            },
        ),
        migrations.CreateModel(
            name='LaboratorySoftware',
            fields=[
                ('id_labsof', models.AutoField(primary_key=True, serialize=False)),
                ('fk_id_lab', models.ForeignKey(blank=True, db_column='fk_id_lab', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='laboratory.laboratory')),
                ('fk_id_sof', models.ForeignKey(blank=True, db_column='fk_id_sof', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='laboratory.software')),
            ],
            options={
                'db_table': 'laboratorios"."laboratorio_software',
            },
        ),
        migrations.CreateModel(
            name='SoftwareReservation',
            fields=[
                ('id_sofres', models.AutoField(primary_key=True, serialize=False)),
                ('fk_id_res', models.ForeignKey(blank=True, db_column='fk_id_res', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='laboratory.reservation')),
                ('fk_id_sof', models.ForeignKey(blank=True, db_column='fk_id_sof', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='laboratory.software')),
            ],
            options={
                'db_table': 'laboratorios"."software_reserva',
            },
        ),
    ]
