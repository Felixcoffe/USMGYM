# Generated by Django 4.1.3 on 2023-07-02 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_día_horario_dia'),
    ]

    operations = [
        migrations.AddField(
            model_name='horario',
            name='bloques',
            field=models.IntegerField(null=True),
        ),
    ]
