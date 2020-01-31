from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('cadastro/pf',cadastrar_pessoa_fisica),
    path('cadastro/pf/acessibilidade', acessibilidade_cadastro),
    path('pj/<int:id>', detalhar_empresa),
    path('cadastro/pj', cadastrar_empresa),
    path('editar/pj/<int:id>', editar_empresa),
    path('remover/pj/<int:id>', remover_empresa),
    path('admin/', admin.site.urls),
    path('', include('vaga.urls')),
]
