from django.contrib import admin
from django.urls import path, include
from usuarios.views import *
from curriculo.views import *

urlpatterns = [
    path('', home),
    path('curriculo/', include('curriculo.urls')),
    path('admin/', admin.site.urls),
    path('vagas/', include('vaga.urls')),
    path('dados/', include('usuarios.urls')),
]    
