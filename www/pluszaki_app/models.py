from django.db import models

class Pluszak(models.Model):
    imie = models.CharField(max_length=100)
    gatunek = models.CharField(max_length=100)
    opis = models.TextField(blank=True)
    data_dodania = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.imie

