from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    # path('ekipa/', views.lista_pluszakow, name='test_widok'),
    path("ekipa/", TemplateView.as_view(template_name="pluszak.html")),
    path("", TemplateView.as_view(template_name="glowna.html")),
    # path('', views.lista_pluszakow, name='gl_widok'),
]