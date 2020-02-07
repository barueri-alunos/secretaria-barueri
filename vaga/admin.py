from django.contrib import admin
from .models import *
from usuarios.export import ExportCsvMixin


class VagasAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('titulo_vaga', 'area_vaga', 'empresa', 'data_abertura', 'ativo')
    search_fields = ['titulo_vaga', 'area_vaga', 'empresa', 'data_abertura', 'ativo']
    actions = ['export_as_csv']
    
# Register your models here.
admin.site.register(Vaga)
admin.site.register(Detalhes)