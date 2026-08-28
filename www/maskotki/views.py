from django.shortcuts import render
from .forms import FormularzKontaktowy  # Importujemy Twój formularz

def pokaz_formularz(request):
    # Logika: Czy użytkownik kliknął przycisk Wyślij? (POST)
    if request.method == 'POST':
        formularz = FormularzKontaktowy(request.POST) # Wkładamy wpisane dane do "pudełka"
        
        if formularz.is_valid(): # Django automatycznie sprawdza logikę (czy pola są pełne itp.)
            dane = formularz.cleaned_data # Wyciągamy bezpieczne dane
            imie_uzytkownika = dane['imie']
            
            # Jeśli wszystko jest OK, wyświetlamy stronę sukcesu
            return render(request, 'pokaz_dane.html', {'imie': imie_uzytkownika})
            
    else:
        # Jeśli użytkownik dopiero wszedł na stronę (GET) – dajemy mu pusty formularz
        formularz = FormularzKontaktowy()

    # Wyświetlamy stronę z formularzem
    return render(request, 'formularz.html', {'formularz': formularz})
