from django import forms
from .models import *

class PessoaFisicaForm(forms.ModelForm):
    class Meta:
        model = PessoaFisica
        fields = [ 
            'first_name', 
            'last_name',
            'username', 
            'password',
            'nome',
            'genero',
            'data_nascimento',
            'estado_civil',
            'cpf',
            'telefone_fixo',
            'celular',
           ]
        

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
        fields = [
            'logradouro', 
            'numero', 
            'complemento', 
            'cidade', 
            'estado', 
            'cep', 
            ]


class AcessibilidadeForm(forms.ModelForm):

    class Meta:
        model = Acessibilidade
        fields = [
            'outros_tipos_deficiencia', 
            'tipo_deficiencia', 
            'cid', 
            ]


        fields = '__all__'

class Avaliacao_SecretariaForm(forms.ModelForm):

    class Meta:
        model = Avaliacao_Secretaria
        fields = '__all__'
