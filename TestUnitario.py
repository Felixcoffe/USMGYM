import unittest
from datetime import datetime
from reservation_system import ReservationSystem, Reservation

class ReservationSystemTest(unittest.TestCase):
    def setUp(self):
        self.reservation_system = ReservationSystem()
    
    def test_add_reservation(self):
        # Crear una reserva con rut, nombre y carrera técnica
        reservation = Reservation("12345678-9", "John Doe", "Ingeniería Informática", datetime(2023, 6, 27, 9, 0))
        
        # Agregar la reserva al sistema
        self.reservation_system.add_reservation(reservation)
        
        # Verificar que la reserva esté en la lista de reservas del sistema
        self.assertIn(reservation, self.reservation_system.reservations)
    
    def test_remove_reservation(self):
        # Crear una reserva con rut, nombre y carrera técnica
        reservation = Reservation("12345678-9", "John Doe", "Ingeniería Informática", datetime(2023, 6, 27, 9, 0))
        
        # Agregar la reserva al sistema
        self.reservation_system.add_reservation(reservation)
        
        # Eliminar la reserva del sistema
        self.reservation_system.remove_reservation(reservation)
        
        # Verificar que la reserva no esté en la lista de reservas del sistema
        self.assertNotIn(reservation, self.reservation_system.reservations)
    
    def test_get_available_slots(self):
        # Crear algunas reservas con rut, nombre y carrera técnica
        reservation1 = Reservation("12345678-9", "John Doe", "Ingeniería Informática", datetime(2023, 6, 27, 9, 0))
        reservation2 = Reservation("98765432-1", "Jane Smith", "Administración de Empresas", datetime(2023, 6, 27, 10, 0))
        reservation3 = Reservation("56789012-3", "Alice Johnson", "Diseño Gráfico", datetime(2023, 6, 27, 11, 0))
        
        # Agregar las reservas al sistema
        self.reservation_system.add_reservation(reservation1)
        self.reservation_system.add_reservation(reservation2)
        self.reservation_system.add_reservation(reservation3)
        
        # Obtener los horarios disponibles para reservar
        available_slots = self.reservation_system.get_available_slots(datetime(2023, 6, 27))
        
        # Verificar que los horarios disponibles no incluyan los horarios ya reservados
        self.assertNotIn(datetime(2023, 6, 27, 9, 0), available_slots)
        self.assertNotIn(datetime(2023, 6, 27, 10, 0), available_slots)
        self.assertNotIn(datetime(2023, 6, 27, 11, 0), available_slots)
        
        # Verificar que los horarios disponibles sí incluyan otros horarios disponibles
        self.assertIn(datetime(2023, 6, 27, 8, 0), available_slots)
        self.assertIn(datetime(2023, 6, 27, 12, 0), available_slots)
        self.assertIn(datetime(2023, 6, 27, 13, 0), available_slots)

if __name__ == '__main__':
    unittest.main()