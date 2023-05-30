from django.db import models

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Horario(models.Model):
    id_horario = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_final = models.TimeField()
    estado = models.BooleanField()
    bloques_totales = models.IntegerField()

    def __str__(self):
        return f"{self.fecha} - {self.hora_inicio} a {self.hora_final}"

class Cupos(models.Model):
    id_horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    hora = models.TimeField()
    cupos_disponibles = models.IntegerField()
    estado = models.BooleanField()

    def __str__(self):
        return f"{self.id_horario} - {self.hora}"

class Cliente(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    rol_usm = models.CharField(max_length=50)
    rut = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre