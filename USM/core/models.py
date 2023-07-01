from django.db import models
import uuid


class Horario(models.Model):
    id_horario = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_final = models.TimeField()
    estado = models.BooleanField(default=True)
    bloques_totales = models.IntegerField()
    bloques_disponibles = models.IntegerField()

    def __str__(self):
        return str(self.id_horario)

    def restar_cupos(self, cantidad):
        self.bloques_totales -= cantidad
        self.save()

class Cupos(models.Model):
    id_cupo = models.AutoField(primary_key=True)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    nombre = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)
    rut = models.CharField(max_length=50)

    def __str__(self):
        return f'Cupo {self.id_cupo} - {self.horario}'


class Cliente(models.Model):
    rut = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre