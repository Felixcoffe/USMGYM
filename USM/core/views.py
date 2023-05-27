from django.shortcuts import render,redirect
from core.models import horario
from django.db.models import Q


def home(request):
    return render(request,'core/home.html')


def horario_reservas(request):
    reservas = horario.objects.all()
    # Aquí puedes realizar cualquier otra lógica para filtrar y ordenar las reservas según tus necesidades

    context = {
        'reservas': reservas
    }
    return render(request, 'horario_reservas.html', context)

def hacer_reserva(request):
    if request.method == 'POST':
        fecha = request.POST['fecha']
        hora_inicio = request.POST['hora_inicio']
        hora_fin = request.POST['hora_fin']

        # Validar si hay cupo disponible para hacer la reserva
        reserva_existente = horario.objects.filter(fecha=fecha, hora_inicio=hora_inicio, hora_fin=hora_fin).first()
        if reserva_existente:
            if reserva_existente.cupo > 0:
                reserva_existente.cupo -= 1
                reserva_existente.save()
            else:
                # No hay cupo disponible, mostrar mensaje de error o redireccionar a otra página
                pass
        else:
            # No existe reserva en ese horario, mostrar mensaje de error o redireccionar a otra página
            pass

        return redirect('horario_reservas')
# Create your views here.
