from django.shortcuts import render
from .models import Pluszak

def lista_pluszakow(request):
    wszystkie_pluszaki = Pluszak.objects.all() 
    return render(request, 'pluszak.html', {'Pluszaki': wszystkie_pluszaki})

