from django.shortcuts import render
from .models import Pluszak  # importujesz swój model

def lista_zadan(request):
    wszystkie_pluszaki = Pluszak.objects.all() 
    return render(request, 'pluszak.html', {'Pluszaki': wszystkie_pluszaki})

