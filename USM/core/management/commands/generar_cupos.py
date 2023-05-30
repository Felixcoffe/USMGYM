from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from core.models import Horario, Cupos

class Command(BaseCommand):
    help = 'Genera automáticamente registros de Horario y Cupos'

    def handle(self, *args, **options):
        # Obtener la fecha actual
        fecha_actual = datetime.now().date()

        # Obtener el próximo día lunes
        dia_lunes = fecha_actual + timedelta(days=(7 - fecha_actual.weekday()))

        # Generar registros de Horario y Cupos para los próximos 7 días, omitiendo los domingos
        for i in range(7):
            fecha = dia_lunes + timedelta(days=i)

            # Omitir los registros para los domingos
            if fecha.weekday() == 6:
                continue

            # Generar registros de Horario para cada hora desde las 8 am hasta las 5 pm
            for hora in range(8, 17):
                hora_inicio = datetime(fecha.year, fecha.month, fecha.day, hora, 0)
                hora_final = hora_inicio + timedelta(hours=1)

                # Crear un registro de Horario
                horario = Horario.objects.create(
                    fecha=fecha,
                    hora_inicio=hora_inicio.time(),
                    hora_final=hora_final.time(),
                    estado=True,
                    bloques_totales=8  # Actualizar el número de cupos a 8
                )

                # Generar los 8 cupos para el horario actual
                for cupo in range(8):
                    Cupos.objects.create(
                        id_horario=horario,
                        hora=hora_inicio.time(),
                        cupos_disponibles=1,
                        estado=True
                    )

        self.stdout.write(self.style.SUCCESS('Base de datos poblada exitosamente'))
