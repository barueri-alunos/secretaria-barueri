from django.contrib import admin
from django.urls import path
from usuarios.models import PessoaJuridica
from usuarios.views import *

urlpatterns = [
    path('cadastro/pessoa_juridica', cadastro_empresa),
    path('admin/', admin.site.urls),
    path('cadastrar/pessoafisica',cadastrar_pessoa_fisica),
]
