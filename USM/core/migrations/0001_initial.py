# Generated by Django 4.1.3 on 2023-05-30 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id_horario', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_final', models.TimeField()),
                ('estado', models.BooleanField()),
                ('bloques_totales', models.IntegerField()),
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.TimeField()),
                ('cupos_disponibles', models.IntegerField()),
                ('estado', models.BooleanField()),
                ('id_horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.horario')),
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
