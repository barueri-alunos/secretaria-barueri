"""secretaria_barueri URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
<<<<<<< HEAD

urlpatterns = [
    path('admin/', admin.site.urls),
=======
from usuarios.views import cadastrar_pessoa_fisica

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('cadastrar/pessoafisica',cadastrar_pessoa_fisica),
>>>>>>> 6903fc8... Importar cadastar_pessoa_fisica da views para urls
=======
    path('cadastrar/pf',cadastrar_pessoa_fisica),
>>>>>>> 1635bf6... Corrigir sintax de cadatsro.html, views e urls.
]
