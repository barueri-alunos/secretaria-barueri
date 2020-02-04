from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('competencia/<int:id>', cadastrar_competencia),
]