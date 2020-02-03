from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD


urlpatterns = [
    path('admin/', admin.site.urls),
    path('vagas/', include('vaga.urls')),
    path('dados/', include('usuarios.urls'))
    path('avaliacao/', )
    path('cadastro/pf', cadastrar_pessoa_fisica),
    path('cadastro/pf/acessibilidade', acessibilidade_cadastro),
    path('cadastro/pj', cadastrar_empresa),
    path('admin/', admin.site.urls),
    path('avaliacao/secretaria', avaliacao_secretaria),
    path('cadastro/', include(usuarios.urls))
]
