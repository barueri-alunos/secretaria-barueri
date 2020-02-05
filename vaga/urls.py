from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('editar/<int:id>', editar_vagas),
    path('deletar/<int:id>', remover_vaga),
    path('detalhes/-<int:id>', detalhe_vaga),
    path('cadastro/<int:id>', cadastro_vaga),
    path('lista/',lista_vaga),
]