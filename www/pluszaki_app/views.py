from django.shortcuts import render
from .models import Pluszak
from django.http import HttpResponse

def lista_pluszakow(request):
    wszystkie_pluszaki = Pluszak.objects.all() 
    return render(request, 'pluszak.html', {'Pluszaki': wszystkie_pluszaki})
# Funkcja tymczasowa do wyświetlenia widoku 

# def lista_pluszakow(request):
#     return HttpResponse("Cześć! To działa, tutaj będą Twoje pluszaki.")