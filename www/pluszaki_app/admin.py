from django.contrib import admin
from .models import Pluszak

# Wyświetlenie listy w admin
class PluszakAdmin(admin.ModelAdmin):
    list_display = ('imie', 'gatunek', 'zapasy')
    
admin.site.register(Pluszak)
admin.site.register(Pluszak, PluszakAdmin)