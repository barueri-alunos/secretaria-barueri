from django.contrib import admin
from django.urls import path
from usuarios.models import PessoaJuridica
from usuarios.views import cadastro_empresa

urlpatterns = [
    path('cadastro/pessoa_juridica', cadastro_empresa),
    path('admin/', admin.site.urls),
]
