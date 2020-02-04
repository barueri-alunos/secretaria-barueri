from django.contrib import admin
from django.urls import path, include
from usuarios.views import home

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('vagas/', include('vaga.urls')),
    path('dados/', include('usuarios.urls')),
]
