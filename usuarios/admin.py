from django.contrib import admin
from usuarios.models import *
from usuarios.export import ExportCsvMixin


class PFAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('nome', 'cpf', 'celular', 'genero', 'ativo')
    ordering = ('-criado_em',)
    search_fields = ['nome', 'cpf', 'celular', 'genero', 'ativo']
    actions = ['export_as_csv']
    

class PJAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('razao_social', 'cnpj', 'contato_empresa')
    search_fields = ['razao_social', 'cnpj', 'contato_empresa']
    actions = ['export_as_csv']
    
    
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'logradouro', 'numero', 'cidade', 'cep')
    search_fields = ['usuario', 'logradouro', 'numero', 'cidade', 'cep']
    
    
admin.site.register(PessoaFisica, PFAdmin)
admin.site.register(PessoaJuridica, PJAdmin)
admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Acessibilidade)