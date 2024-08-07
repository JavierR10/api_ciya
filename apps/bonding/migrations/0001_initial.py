# Generated by Django 5.0.3 on 2024-04-08 04:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id_con', models.AutoField(primary_key=True, serialize=False)),
                ('documento_con', models.CharField(blank=True, max_length=1500, null=True)),
                ('fecha_inicio_con', models.DateField(blank=True, null=True)),
                ('fecha_fin_con', models.DateField(blank=True, null=True)),
                ('fk_id_emp', models.IntegerField()),
                ('fecha_creacion_con', models.DateTimeField(blank=True, null=True)),
                ('fecha_actualizacion_con', models.DateTimeField(blank=True, null=True)),
                ('usuario_creacion_con', models.CharField(blank=True, max_length=255, null=True)),
                ('usuario_actualizacion_con', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_con', models.CharField(blank=True, max_length=50, null=True)),
                ('estado_con', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'vinculacion"."convenio',
            },
        ),
        migrations.CreateModel(
            name='Commissioner',
            fields=[
                ('id_comi', models.AutoField(primary_key=True, serialize=False)),
                ('estado_comi', models.CharField(max_length=15)),
                ('fecha_creacion_comi', models.DateTimeField()),
                ('fecha_actualizacion_comi', models.DateTimeField()),
                ('usuario_creacion_comi', models.CharField(max_length=250)),
                ('usuario_actualizacion_comi', models.CharField(max_length=250)),
                ('fk_id_doc', models.IntegerField(blank=True, null=True)),
                ('fk_id_per', models.IntegerField(blank=True, null=True)),
                ('fk_id_car', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'vinculacion"."comicionado',
            },
        ),
        migrations.CreateModel(
            name='CommissionerVin',
            fields=[
                ('id_comi', models.AutoField(primary_key=True, serialize=False)),
                ('estado_comi', models.CharField(max_length=15)),
                ('fecha_creacion_comi', models.DateTimeField()),
                ('fecha_actualizacion_comi', models.DateTimeField()),
                ('usuario_creacion_comi', models.CharField(max_length=250)),
                ('usuario_actualizacion_comi', models.CharField(max_length=250)),
                ('fk_id_doc', models.IntegerField(blank=True, null=True)),
                ('fk_id_per', models.IntegerField(blank=True, null=True)),
                ('fk_id_car', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'vinculacion"."comicionadovin',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id_emp', models.AutoField(primary_key=True, serialize=False)),
                ('ruc_emp', models.CharField(blank=True, max_length=15, null=True)),
                ('nombre_emp', models.CharField(blank=True, max_length=500, null=True)),
                ('provincia_emp', models.CharField(blank=True, max_length=100, null=True)),
                ('canton_emp', models.CharField(blank=True, max_length=100, null=True)),
                ('direccion_emp', models.CharField(blank=True, max_length=500, null=True)),
                ('latitud_emp', models.FloatField(blank=True, null=True)),
                ('longitud_emp', models.FloatField(blank=True, null=True)),
                ('telefono_emp', models.CharField(blank=True, max_length=150, null=True)),
                ('correo_emp', models.CharField(blank=True, max_length=150, null=True)),
                ('logo_emp', models.CharField(blank=True, max_length=450, null=True)),
                ('tipo_emp', models.CharField(blank=True, max_length=500, null=True)),
                ('estado_emp', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion_emp', models.DateTimeField(blank=True, null=True)),
                ('fecha_actualizacion_emp', models.DateTimeField(blank=True, null=True)),
                ('usuario_creacion_emp', models.CharField(blank=True, max_length=255, null=True)),
                ('usuario_actualizacion_emp', models.CharField(blank=True, max_length=255, null=True)),
                ('parroquia_emp', models.CharField(blank=True, max_length=2500, null=True)),
                ('actividad_emp', models.TextField(blank=True, null=True)),
                ('sector_economico_emp', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'vinculacion"."empresa',
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id_doc', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_doc', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion_doc', models.CharField(blank=True, max_length=300, null=True)),
                ('fecha_creacion_doc', models.DateTimeField(blank=True, null=True)),
                ('fecha_actualizacion_doc', models.DateTimeField(blank=True, null=True)),
                ('usuario_creacion_doc', models.CharField(blank=True, max_length=255, null=True)),
                ('usuario_actualizacion_doc', models.CharField(blank=True, max_length=255, null=True)),
                ('documento_doc', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'db_table': 'vinculacion"."documento',
            },
        ),
        migrations.CreateModel(
            name='ProcessVin',
            fields=[
                ('id_prov', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_prov', models.CharField(max_length=250)),
                ('descripcion_prov', models.TextField()),
                ('estado_prov', models.CharField(max_length=15)),
                ('fecha_creacion_prov', models.DateTimeField()),
                ('fecha_actualizacion_prov', models.DateTimeField()),
                ('usuario_creacion_prov', models.CharField(max_length=250)),
                ('usuario_actualizacion_prov', models.CharField(max_length=250)),
                ('fk_id_doc', models.IntegerField(blank=True, null=True)),
                ('fk_id_per', models.IntegerField(blank=True, null=True)),
                ('fk_id_car', models.IntegerField(blank=True, null=True)),
                ('fk_id_cur', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'vinculacion"."procesovinculacion',
            },
        ),
        migrations.CreateModel(
            name='ProgramVin',
            fields=[
                ('id_prog', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_prog', models.CharField(max_length=250)),
                ('descripcion_prog', models.TextField()),
                ('estado_prog', models.CharField(max_length=15)),
                ('fecha_creacion_prog', models.DateTimeField()),
                ('fecha_actualizacion_prog', models.DateTimeField()),
                ('usuario_creacion_prog', models.CharField(max_length=250)),
                ('usuario_actualizacion_prog', models.CharField(max_length=250)),
                ('fk_id_fac', models.IntegerField(blank=True, null=True)),
                ('archivo_prog', models.CharField(blank=True, max_length=1500, null=True)),
            ],
            options={
                'db_table': 'vinculacion"."programavin',
            },
        ),
        migrations.CreateModel(
            name='RegistrationVin',
            fields=[
                ('id_matr', models.AutoField(primary_key=True, serialize=False)),
                ('estado_matr', models.CharField(max_length=15)),
                ('fecha_creacion_matr', models.DateTimeField()),
                ('fecha_actualizacion_matr', models.DateTimeField()),
                ('usuario_creacion_matr', models.CharField(max_length=250)),
                ('usuario_actualizacion_matr', models.CharField(max_length=250)),
                ('fk_id_est', models.IntegerField(blank=True, null=True)),
                ('fk_id_per', models.IntegerField(blank=True, null=True)),
                ('fk_id_car', models.IntegerField(blank=True, null=True)),
                ('fk_id_cur', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'vinculacion"."matriculavin',
            },
        ),
        migrations.CreateModel(
            name='ScheduleVin',
            fields=[
                ('id_cro', models.AutoField(primary_key=True, serialize=False)),
                ('semanauno_cro', models.TextField()),
                ('semanados_cro', models.TextField()),
                ('semanatres_cro', models.TextField()),
                ('semanacuatro_cro', models.TextField()),
                ('semanacinco_cro', models.TextField()),
                ('semanaseis_cro', models.TextField()),
                ('semanasiete_cro', models.TextField()),
                ('semanaocho_cro', models.TextField()),
                ('semananueve_cro', models.TextField()),
                ('semanadiez_cro', models.TextField()),
                ('semanaonce_cro', models.TextField()),
                ('semanadose_cro', models.TextField()),
                ('semanatrese_cro', models.TextField()),
                ('semanacatorse_cro', models.TextField()),
                ('semanaquinse_cro', models.TextField()),
                ('semanadiecises_cro', models.TextField()),
                ('estado_cro', models.CharField(db_column='estado__cro', max_length=15)),
                ('fecha_creacion_cro', models.DateTimeField()),
                ('fecha_actualizacion_cro', models.DateTimeField()),
                ('usuario_creacion_cro', models.CharField(max_length=250)),
                ('usuario_actualizacion_cro', models.CharField(max_length=250)),
                ('fk_id_prf', models.IntegerField(blank=True, null=True)),
                ('fk_id_per', models.IntegerField(blank=True, null=True)),
                ('fk_id_car', models.IntegerField(blank=True, null=True)),
                ('fk_id_est', models.IntegerField(blank=True, null=True)),
                ('fk_id_doc', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'vinculacion"."cronogramavin',
            },
        ),
        migrations.CreateModel(
            name='TutorVin',
            fields=[
                ('id_tut', models.AutoField(primary_key=True, serialize=False)),
                ('estado_tut', models.CharField(max_length=15)),
                ('fecha_creacion_tut', models.DateTimeField()),
                ('fecha_actualizacion_tut', models.DateTimeField()),
                ('usuario_creacion_tut', models.CharField(max_length=250)),
                ('usuario_actualizacion_tut', models.CharField(max_length=250)),
                ('fk_id_doc', models.IntegerField(blank=True, null=True)),
                ('fk_id_per', models.IntegerField(blank=True, null=True)),
                ('fk_id_car', models.IntegerField(blank=True, null=True)),
                ('fk_id_cur', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'vinculacion"."tutorvin',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id_tip', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tip', models.TextField(blank=True, null=True)),
                ('siglas_tip', models.CharField(blank=True, max_length=50, null=True)),
                ('estado_tip', models.IntegerField(blank=True, null=True)),
                ('fecha_creacion_tip', models.DateTimeField(blank=True, null=True)),
                ('fecha_actualizacion_tip', models.DateTimeField(blank=True, null=True)),
                ('usuario_creacion_tip', models.CharField(blank=True, max_length=255, null=True)),
                ('usuario_actualizacion_tip', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'vinculacion"."tipo',
            },
        ),
        migrations.CreateModel(
            name='TypeVin',
            fields=[
                ('id_tipo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipo', models.CharField(max_length=250)),
                ('siglas_tipo', models.CharField(max_length=250)),
                ('descripcion_tipo', models.TextField()),
                ('estado_tipo', models.CharField(max_length=15)),
                ('fecha_creacion_tipo', models.DateTimeField()),
                ('fecha_actualizacion_tipo', models.DateTimeField()),
                ('usuario_creacion_tipo', models.CharField(max_length=250)),
                ('usuario_actualizacion_tipo', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'vinculacion"."tipovin',
            },
        ),
        migrations.CreateModel(
            name='CareerAgreement',
            fields=[
                ('id_con_car', models.AutoField(primary_key=True, serialize=False)),
                ('fk_id_car', models.BigIntegerField(blank=True, null=True)),
                ('fk_id_con', models.ForeignKey(blank=True, db_column='fk_id_con', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bonding.agreement')),
            ],
            options={
                'db_table': 'vinculacion"."convenio_carrera',
            },
        ),
        migrations.CreateModel(
            name='GroupVin',
            fields=[
                ('id_grupo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_grupo', models.CharField(max_length=250)),
                ('numero_grupo', models.TextField()),
                ('estado_grupo', models.CharField(max_length=15)),
                ('fecha_creacion_grupo', models.DateTimeField()),
                ('fecha_actualizacion_grupo', models.DateTimeField()),
                ('usuario_creacion_grupo', models.CharField(max_length=250)),
                ('usuario_actualizacion_grupo', models.CharField(max_length=250)),
                ('fk_id_cur', models.IntegerField(blank=True, null=True)),
                ('fk_id_con', models.ForeignKey(blank=True, db_column='fk_id_con', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bonding.agreement')),
                ('fk_id_emp', models.ForeignKey(blank=True, db_column='fk_id_emp', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bonding.company')),
                ('fk_id_prov', models.ForeignKey(blank=True, db_column='fk_id_prov', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bonding.processvin')),
            ],
            options={
                'db_table': 'vinculacion"."grupovin',
            },
        ),
        migrations.CreateModel(
            name='ProjectVin',
            fields=[
                ('id_proy', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_proy', models.CharField(max_length=250)),
                ('descripcion_proy', models.TextField()),
                ('estado_proy', models.CharField(max_length=15)),
                ('fecha_creacion_proy', models.DateTimeField()),
                ('fecha_actualizacion_proy', models.DateTimeField()),
                ('usuario_creacion_proy', models.CharField(max_length=250)),
                ('usuario_actualizacion_proy', models.CharField(max_length=250)),
                ('fk_id_car', models.IntegerField(blank=True, null=True)),
                ('fk_id_per', models.IntegerField(blank=True, null=True)),
                ('fk_id_prog', models.ForeignKey(blank=True, db_column='fk_id_prog', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bonding.programvin')),
            ],
            options={
                'db_table': 'vinculacion"."proyectovin',
            },
        ),
        migrations.AddField(
            model_name='processvin',
            name='fk_id_proy',
            field=models.ForeignKey(blank=True, db_column='fk_id_proy', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bonding.projectvin'),
        ),
        migrations.CreateModel(
            name='DocumentsVin',
            fields=[
                ('id_doc', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_doc', models.CharField(max_length=250)),
                ('descripcion_doc', models.CharField(max_length=250)),
                ('estado_doc', models.CharField(max_length=15)),
                ('fecha_creacion_doc', models.DateTimeField()),
                ('fecha_actualizacion_doc', models.DateTimeField()),
                ('usuario_creacion_doc', models.CharField(max_length=250)),
                ('usuario_actualizacion_doc', models.CharField(max_length=250)),
                ('documento_doc', models.CharField(max_length=250)),
                ('fk_id_proy', models.ForeignKey(blank=True, db_column='fk_id_proy', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bonding.projectvin')),
            ],
            options={
                'db_table': 'vinculacion"."documentovin',
            },
        ),
        migrations.CreateModel(
            name='IntegranteVin',
            fields=[
                ('id_inte', models.AutoField(primary_key=True, serialize=False)),
                ('estado_inte', models.CharField(max_length=15)),
                ('fecha_creacion_inte', models.DateTimeField()),
                ('fecha_actualizacion_inte', models.DateTimeField()),
                ('usuario_creacion_inte', models.CharField(max_length=250)),
                ('usuario_actualizacion_inte', models.CharField(max_length=250)),
                ('fk_id_grupo', models.ForeignKey(blank=True, db_column='fk_id_grupo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bonding.groupvin')),
                ('fk_id_matr', models.ForeignKey(blank=True, db_column='fk_id_matr', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bonding.registrationvin')),
            ],
            options={
                'db_table': 'vinculacion"."integrantevin',
            },
        ),
        migrations.AddField(
            model_name='processvin',
            name='fk_id_tut',
            field=models.ForeignKey(blank=True, db_column='fk_id_tut', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bonding.tutorvin'),
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id_proc', models.AutoField(primary_key=True, serialize=False)),
                ('fk_id_per', models.IntegerField(blank=True, null=True)),
                ('fk_id_con', models.IntegerField(blank=True, null=True)),
                ('fk_id_doc', models.IntegerField(blank=True, null=True)),
                ('tema_proc', models.TextField(blank=True, null=True)),
                ('fecha_creacion_proc', models.DateTimeField(blank=True, null=True)),
                ('fecha_actualizacion_proc', models.DateTimeField(blank=True, null=True)),
                ('usuario_creacion_proc', models.CharField(blank=True, max_length=255, null=True)),
                ('usuario_actualizacion_proc', models.CharField(blank=True, max_length=255, null=True)),
                ('fk_id_tip', models.ForeignKey(blank=True, db_column='fk_id_tip', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bonding.type')),
            ],
            options={
                'db_table': 'vinculacion"."proceso',
            },
        ),
        migrations.AddField(
            model_name='tutorvin',
            name='fk_id_tipo',
            field=models.ForeignKey(blank=True, db_column='fk_id_tipo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bonding.typevin'),
        ),
        migrations.AddField(
            model_name='registrationvin',
            name='fk_id_tipo',
            field=models.ForeignKey(blank=True, db_column='fk_id_tipo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bonding.typevin'),
        ),
        migrations.AddField(
            model_name='processvin',
            name='fk_id_tipo',
            field=models.ForeignKey(blank=True, db_column='fk_id_tipo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bonding.typevin'),
        ),
    ]
