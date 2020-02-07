from django import forms
from .models import *

class VagaForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})
    
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
        'detalhes_vaga'
        ]
        

     