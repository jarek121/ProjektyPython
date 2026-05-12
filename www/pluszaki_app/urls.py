from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.lista_pluszakow, name='test_widok'),
]