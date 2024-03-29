# Generated by Django 4.1.3 on 2023-05-31 05:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id_horario', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_final', models.TimeField()),
                ('estado', models.BooleanField(default=True)),
                ('bloques_totales', models.IntegerField(default=20)),
                ('bloques_disponibles', models.IntegerField(default=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cupos',
            fields=[
                ('id_cupo', models.AutoField(primary_key=True, serialize=False)),
                ('hora', models.TimeField()),
                ('cupos_disponibles', models.IntegerField(default=0)),
                ('estado', models.BooleanField(default=True)),
                ('nombre', models.CharField(max_length=50)),
                ('carrera', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=50)),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.horario')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol_usm', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('carrera', models.CharField(max_length=50)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
    ]
