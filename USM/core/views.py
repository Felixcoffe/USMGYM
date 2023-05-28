from django.shortcuts import render,redirect
from django.db.models import Q


def home(request):
    return render(request,'core/home.html')

def horario(request):
    return render(request,'core/horario.html')
