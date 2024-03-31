# Generated by Django 5.0.3 on 2024-03-31 05:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convocatory',
            fields=[
                ('id_conv', models.AutoField(primary_key=True, serialize=False)),
                ('documento_conv', models.CharField(max_length=500)),
                ('estado_conv', models.CharField(max_length=500)),
                ('flag_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'investigacion"."convocatoria',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id_gru', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_gru', models.CharField(max_length=200)),
                ('tipo_gru', models.CharField(max_length=100)),
                ('flag_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'investigacion"."grupo',
            },
        ),
        migrations.CreateModel(
            name='Linea',
            fields=[
                ('id_lin', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion_lin', models.TextField()),
                ('estado_lin', models.IntegerField()),
                ('nombre_lin', models.TextField()),
                ('flag_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'investigacion"."linea',
            },
        ),
        migrations.CreateModel(
            name='PaisBm',
            fields=[
                ('id_bm', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_bm', models.CharField(max_length=100)),
                ('continente_bm', models.CharField(max_length=100)),
                ('flag_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'investigacion"."pais_bm',
            },
        ),
        migrations.CreateModel(
            name='PaisSv',
            fields=[
                ('id_sv', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_sv', models.CharField(max_length=100)),
                ('continente_sv', models.CharField(max_length=100)),
                ('flag_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'investigacion"."pais_sv',
            },
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id_tip', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tip', models.CharField(max_length=50)),
                ('flag_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'investigacion"."tipo_proyecto',
            },
        ),
        migrations.CreateModel(
            name='Sublinea',
            fields=[
                ('id_sub', models.AutoField(primary_key=True, serialize=False)),
                ('fk_id_car', models.IntegerField()),
                ('nombre_sub', models.TextField()),
                ('descripcion_sub', models.TextField()),
                ('estado_sub', models.IntegerField()),
                ('flag_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'investigacion"."sublinea',
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id_equ', models.AutoField(primary_key=True, serialize=False)),
                ('fk_id_doc', models.IntegerField()),
                ('fk_id_gru', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='investigacion.group')),
                ('flag_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'investigacion"."equipo',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id_pro', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_pro', models.TextField()),
                ('grupo_investigacion_pro', models.IntegerField()),
                ('programa_pro', models.IntegerField()),
                ('fecha_aprobacion_pro', models.IntegerField()),
                ('fk_id_lin', models.IntegerField()),
                ('fk_id_car', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='public.collegecareer')),
                ('fk_id_doc', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='public.teacher')),
                ('fk_id_tip', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='investigacion.projecttype')),
                ('flag_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'investigacion"."proyecto',
            },
        ),
        migrations.CreateModel(
            name='TopicBank',
            fields=[
                ('id_ban', models.AutoField(primary_key=True, serialize=False)),
                ('fk_id_doc', models.IntegerField()),
                ('fk_id_sub', models.IntegerField()),
                ('tema_ban', models.CharField(max_length=500)),
                ('descripcion_ban', models.TextField()),
                ('archivo_adjunto_ban', models.TextField()),
                ('fecha_creacion_ban', models.DateTimeField(auto_now=True)),
                ('fecha_actualizacion_ban', models.DateTimeField(auto_now=True)),
                ('usuario_creacion_ban', models.CharField(max_length=255)),
                ('usuario_actualizacion_ban', models.CharField(max_length=255)),
                ('validacion_ban', models.CharField(max_length=100)),
                ('estado_ban', models.CharField(max_length=50)),
                ('fk_id_lin', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='investigacion.linea')),
                ('flag_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'investigacion"."banco_temas',
            },
        ),
    ]
