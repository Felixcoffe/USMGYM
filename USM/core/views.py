from django.shortcuts import render,redirect
from django.db.models import Q
from .models import Horario

def home(request):
    return render(request,'core/home.html')

def horario(request):
    horario= Horario.objects.all()
    context= {'horarios':horario}
    return render(request,'core/horario.html', context)
