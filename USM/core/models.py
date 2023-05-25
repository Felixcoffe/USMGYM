from django.db import models

# Create your models here.
class usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)

class horario(models.Model):
    id_horario = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    Estado = models.BooleanField()
    bloques_totales = models.IntegerField()

class cupos(models.Model):
    id_horario = models.ForeignKey(horario, on_delete=models.CASCADE)
    hora = models.DateField()
    cupos = models.IntegerField()
    Estado = models.BooleanField()

class cliente(models.Model):
    rol_usm = models.CharField(max_length=50)
    rut = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)