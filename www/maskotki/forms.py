from django import forms

class FormularzKontaktowy(forms.Form):
    imie = forms.CharField(label="Twoje imię", max_length=100)
    wiadomosc = forms.CharField(label="Treść", widget=forms.TextInput)
