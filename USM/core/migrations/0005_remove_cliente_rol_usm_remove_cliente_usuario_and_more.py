# Generated by Django 4.1.3 on 2023-07-01 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_cupos_cupos_disponibles_remove_cupos_hora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='rol_usm',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
