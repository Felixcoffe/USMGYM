from django.shortcuts import render
from datetime import datetime, timedelta, date
from .models import Horario

def home(request):
    return render(request,'core/home.html')



import datetime

import datetime

def horario(request):
    # Obtener la fecha actual
    now = datetime.datetime.now()
    
    # Obtener el día de la semana actual (0: lunes, 1: martes, ..., 6: domingo)
    dia_actual = now.weekday()
    
    # Obtener una lista de días de la semana
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    
    # Reorganizar la lista de días para que comience con el día actual
    dias = dias[dia_actual:] + dias[:dia_actual]
    
    # Obtener una lista de horas del 1 al 11
    horas = [str(i) for i in range(1, 12)]
    
    # Obtener los horarios para el día de la semana actual
    horarios = Horario.objects.filter(fecha__week_day=dia_actual)
    
    context = {
        'horarios': horarios,
        'dias': dias,
        'horas': horas
    }
    
    return render(request, 'core/horario.html', context)