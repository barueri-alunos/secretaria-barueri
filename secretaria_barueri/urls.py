from django.contrib import admin
from django.urls import path
from usuarios.models import PessoaJuridica
from usuarios.views import *

urlpatterns = [
    path('cadastro/pf',cadastrar_pessoa_fisica),
    path('cadastro/pj', cadastrar_empresa),
    path('admin/', admin.site.urls),
    path('cadastro/pf/acessibilidade', acessibilidade_cadastro),
    path('cadastro/vaga', cadastro_vaga),
]
