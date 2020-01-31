from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('vagas/editar/<int:id>', editar_vagas),
    path('vagas/deletar/<int:id>', remover_vaga),
]