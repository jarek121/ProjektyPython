from django.urls import path
from . import views

urlpatterns = [
    path('ekipa/', views.lista_pluszakow, name='test_widok'),
    path('', views.lista_pluszakow, name='gl_widok'),
]