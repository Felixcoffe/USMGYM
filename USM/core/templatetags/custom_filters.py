from django import template

register = template.Library()

@register.filter
def get_cupo_by_day_and_hour(horarios, dia, hora):
    for horario in horarios:
        if horario.fecha.weekday() == int(dia) and horario.hora_inicio.hour == int(hora):
            return horario.cupos.first()
    return None


@register.filter
def translate_day(day):
    translations = {
        'Monday': 'Lunes',
        'Tuesday': 'Martes',
        'Wednesday': 'Miércoles',
        'Thursday': 'Jueves',
        'Friday': 'Viernes',
        'Saturday': 'Sábado',
        'Sunday': 'Domingo',
    }
    return translations.get(day, day)