from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('cadastro/pf',cadastrar_pessoa_fisica),
    path('cadastro/pf/acessibilidade', acessibilidade_cadastro),
    path('cadastro/pj', cadastrar_empresa),
    path('admin/', admin.site.urls),
    path('', include('vaga.urls')),
]
