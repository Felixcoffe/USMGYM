from django.shortcuts import render,redirect
from datetime import datetime, timedelta, date
from .models import Horario,Cupos

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
        now = date.today()
        horarios = Horario.objects.filter(fecha=now)
        dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        dia_actual = now.weekday()
        dias = dias[dia_actual:] + dias[:dia_actual]
        horas = [str(i) for i in range(1, 12)]

        context = {
            'horarios': horarios,
            'dias': dias,
            'horas': horas
        }

        return render(request, 'core/horario.html', context)