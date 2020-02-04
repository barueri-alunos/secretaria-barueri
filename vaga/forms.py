from django import forms
from .models import *

class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = ['titulo_vaga',
        'responsavel_vaga',
        'contato_secretaria',
        'area_vaga',
        'telefone',
        'quantidade_vagas',
        'salario',
        'dias_trabalho',
        'horario_inicio',
        'horario_final',
        'beneficios',
        'escolaridade',
        'data_abertura',
        'detalhes']
        

     