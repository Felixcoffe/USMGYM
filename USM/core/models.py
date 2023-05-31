from django.db import models
import uuid

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre



class Horario(models.Model):
    id_horario = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4, editable=False)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_final = models.TimeField()
    estado = models.BooleanField(default=True)
    bloques_totales = models.IntegerField(default=20)
    bloques_disponibles = models.IntegerField(default=20)

    def __str__(self):
        return self.id_horario


    def restar_cupos(self, cantidad):
        self.bloques_totales -= cantidad
        self.save()

class Cupos(models.Model):
    id_cupo = models.AutoField(primary_key=True)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    hora = models.TimeField()
    cupos_disponibles = models.IntegerField(default=0)
    estado = models.BooleanField(default=True)
    nombre = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)
    rut = models.CharField(max_length=50)

    def __str__(self):
        return f'Cupo {self.id_cupo} - {self.horario}'


class Cliente(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    rol_usm = models.CharField(max_length=50)
    rut = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre