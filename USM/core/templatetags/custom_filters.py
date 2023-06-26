from django import template

register = template.Library()

@register.filter
def get_cupo_by_day_and_hour(horarios, dia, hora):
    for horario in horarios:
        if horario.fecha.weekday() == int(dia) and horario.hora_inicio.hour == int(hora):
            return horario.cupos.first()
    return None