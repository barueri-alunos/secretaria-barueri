from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include
from usuarios.views import *

urlpatterns = [
    path('cadastro/pf',cadastrar_pessoa_fisica),
    path ('cadastro/pf/atualizar/<int:id>',atualizar_cadastro),
    path ('cadastro/pf/deletar/int:id>',deletar_cadastro),
    path('cadastro/pf/acessibilidade', acessibilidade_cadastro),
    path('pf/detalhes/<int:id>',detalhes_pessoa_fisica),
    path('pf/editar/<int:id>', atualizar_pessoa_fisica),
    path('pf/remover/<int:id>', deletar_pessoa_fisica),
    path('pj/detalhes/<int:id>', detalhar_empresa),
    path('cadastro/pj', cadastrar_empresa),
    path('pj/editar/<int:id>', editar_empresa),
    path('pj/remover/<int:id>', remover_empresa),
]
