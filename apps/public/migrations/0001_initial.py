# Generated by Django 5.0.3 on 2024-03-30 21:49

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('flag_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_prf', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_prf', models.CharField(max_length=40)),
                ('descripcion_prf', models.TextField()),
            ],
            options={
                'db_table': 'perfil',
            },
        ),
        migrations.CreateModel(
            name='universidad',
            fields=[
                ('flag_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_uni', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_uni', models.TextField()),
                ('direccion_uni', models.CharField(blank=True, max_length=40, null=True)),
                ('ruc_uni', models.CharField(max_length=40)),
                ('telefono_uni', models.CharField(max_length=40)),
                ('mision_uni', models.TextField()),
                ('vision_uni', models.TextField()),
                ('email_uni', models.CharField(blank=True, max_length=40, null=True)),
                ('facebook_uni', models.CharField(max_length=40)),
                ('twitter_uni', models.CharField(max_length=40)),
                ('instagram_uni', models.CharField(max_length=40)),
                ('pagina_web_uni', models.CharField(max_length=30)),
                ('sede_uni', models.CharField(max_length=50)),
                ('logo_uni', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'universidad',
            },
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('flag_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_usu', models.AutoField(primary_key=True, serialize=False)),
                ('correo_usu', models.EmailField(max_length=40, unique=True, validators=[django.core.validators.EmailValidator])),
                ('password_usu', models.TextField()),
                ('nombre_usu', models.CharField(max_length=40)),
                ('apellido_usu', models.CharField(max_length=40)),
                ('estado_usu', models.IntegerField(default=1)),
                ('fk_id_prf', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='public.profile')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='profileUsers',
            fields=[
                ('flag_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_perusu', models.AutoField(primary_key=True, serialize=False)),
                ('fk_id_per', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='public.profile')),
                ('fk_id_usu', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='public.users')),
            ],
            options={
                'db_table': 'perfil_usuario',
            },
        ),
    ]
