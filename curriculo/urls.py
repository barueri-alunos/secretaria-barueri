from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('cadastrar/', cadastrar_competencia),
    path('deletar/', deletar_competencia),
    path('atualizar/', atualizar_competencia),
    path('detalhes/', detalhes_competencia),
]