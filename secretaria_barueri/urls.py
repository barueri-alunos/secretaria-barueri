from django.contrib import admin
from django.urls import path, include
from usuarios.views import *

urlpatterns = [
    path('vaga/', include('vaga.urls')),
    path('cadastro/pf',cadastrar_pessoa_fisica),
    path('cadastro/pf/acessibilidade', acessibilidade_cadastro),
    path('cadastro/pj', cadastrar_empresa),
    path('admin/', admin.site.urls),
    path('vagas/', include('vaga.urls')),
    path('dados/', include('usuarios.urls'))
]
