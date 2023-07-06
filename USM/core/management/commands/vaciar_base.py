from django.core.management.base import BaseCommand
from core.models import Horario, Cupos

class Command(BaseCommand):
    help = 'Vacía la base de datos eliminando todos los registros de Horario y Cupos'

    def handle(self, *args, **options):
        # Eliminar todos los registros de Cupos
        Cupos.objects.all().delete()

        # Eliminar todos los registros de Horario
        Horario.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Base de datos vaciada exitosamente'))
