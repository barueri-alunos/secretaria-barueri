from django import forms
from usuarios.models import *

class PessoaFisicaForm(forms.ModelForm):
    class Meta:
        model = PessoaFisica
        fields = [ 'first_name', 'last_name', 'username', 'password']
        
class PessoaJuridicaForm(forms.ModelForm):
    class Meta:
        model = PessoaJuridica
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'nome_fantasia', 
            'razao_social', 
            'cnpj', 
            'contato_empresa', 
            'ramo_atividade', 
            'numero_funcionarios', 
            'numero_pcds'
            ]

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'

class AcessibilidadeForm(forms.ModelForm): 
    class Meta:
        Model = Acessibilidade 
        fields = '__all__'

