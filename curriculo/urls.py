from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('deletar/competencia/', deletar_competencia),
    path('atualizar/competencia/', atualiza_competencia),
    path('detalhes/competencia/', detalhes_competencia),
    path('competencia/', cadastrar_competencia),
]