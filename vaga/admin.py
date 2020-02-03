from django.contrib import admin
from .models import *


class VagasAdmin(admin.ModelAdmin):
    list_display = ('titulo_vaga', 'area_vaga', 'empresa', 'data_abertura', 'ativo')
    search_fields = ['titulo_vaga', 'area_vaga', 'empresa', 'data_abertura', 'ativo']
    
# Register your models here.
admin.site.register(Vaga)