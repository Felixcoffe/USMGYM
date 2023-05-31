import uuid
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from core.models import Horario

class Command(BaseCommand):
    help = 'Genera automáticamente registros de Horario'

    def handle(self, *args, **options):
        # Obtener la fecha actual
        fecha_actual = datetime.now().date()

        # Obtener el próximo día lunes
        dia_lunes = fecha_actual + timedelta(days=(7 - fecha_actual.weekday()))

        # Generar registros de Horario para los próximos 7 días, omitiendo los domingos y sábados
        for i in range(7):
            fecha = dia_lunes + timedelta(days=i)

            # Omitir los registros para los domingos y sábados
            if fecha.weekday() in [6, 5]:
                continue

            # Generar registros de Horario para cada hora desde las 8 am hasta las 7 pm
            for hora in range(8, 20):
                hora_inicio = datetime(fecha.year, fecha.month, fecha.day, hora, 0)
                hora_final = hora_inicio + timedelta(minutes=70)

                # Crear un ID único para el horario
                id_horario = uuid.uuid4()

                # Calcular la cantidad de bloques
                minutos_totales = (hora_final - hora_inicio).total_seconds() // 60
                bloques_totales = 20
                bloques_disponibles = bloques_totales

                # Crear un registro de Horario
                horario = Horario(
                    id_horario=id_horario,
                    fecha=fecha,
                    hora_inicio=hora_inicio.time(),
                    hora_final=hora_final.time(),
                    estado=True,
                    bloques_totales=bloques_totales,
                    bloques_disponibles=bloques_disponibles
                )
                horario.save()

        self.stdout.write(self.style.SUCCESS('Base de datos poblada exitosamente'))
