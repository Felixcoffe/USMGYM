from django.shortcuts import render,redirect
from datetime import datetime, timedelta, date
from .models import Horario,Cupos
from django.utils import timezone


def home(request):
    return render(request,'core/home.html')



def horario(request):
    if request.method == 'POST':
        rut = request.POST['rut']
        nombre = request.POST['nombre']
        carrera = request.POST['carrera']
        horario_id = int(request.POST['horario_id'])

        horario = Horario.objects.get(id_horario=horario_id)

        # Crear un nuevo objeto Cupos
        cupo = Cupos(horario=horario, rut=rut, nombre=nombre, carrera=carrera)
        cupo.save()

        # Restar 1 a bloques_disponibles del horario
        horario.bloques_disponibles -= 1
        horario.save()

        return redirect('horario')
    else:
        # Obtén los horarios y otros datos necesarios
        now = timezone.now().date()
        dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        dia_actual = now.weekday()
        
        if dia_actual == 6:  # Si es domingo, ajusta el día actual al lunes más cercano
            dia_actual = 0
        
        dias = dias_semana[dia_actual:] + dias_semana[:dia_actual]
        horas = [int(i) for i in range(1, 13)]

        # Obtén el inicio de la semana
        inicio_semana = now 
        # Obtén el final de la semana
        fin_semana = inicio_semana + timedelta(days=6)

        # Obtén todos los horarios de la semana actual
        horarios = Horario.objects.filter(fecha__range=[inicio_semana, fin_semana])

        context = {
            'horarios': horarios,
            'dias': dias,
            'horas': horas
        }

        return render(request, 'core/horario.html', context)
