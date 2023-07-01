from django.contrib import admin
from .models import Horario, Cupos, Cliente

class cuposadmin(admin.ModelAdmin):
    list_display = ("id_cupo", "horario","estado","nombre","carrera","rut")
    list_filter= ("id_cupo","nombre","rut","carrera")
    search_fields = ("id_cupo","nombre","rut","carrera")
class horarioadmin(admin.ModelAdmin):
    list_display = ("fecha","hora_inicio","hora_final","bloques_totales", "bloques_disponibles")
    search_fields =("fecha","hora_inicio","hora_final","bloques_totales", "bloques_disponibles")
class clienteadmin (admin.ModelAdmin):
    list_display= ("rut","nombre","carrera")
    list_filter = ("rut", "nombre","carrera")
    search_fields = ("rut", "nombre","carrera")

admin.site.register(Horario,horarioadmin)
admin.site.register(Cupos,cuposadmin)
admin.site.register(Cliente,clienteadmin)
# Register your models here.
