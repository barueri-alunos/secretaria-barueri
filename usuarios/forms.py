from django import forms
from .models import *
from .choices import generos, estado, estados

class PessoaFisicaForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs.update({'class':'form-control'})
    class Meta:
        model = PessoaFisica
        fields = [ 
            'first_name', 
            'last_name',
            'username', 
            'password',
            'data_nascimento',
            'estado_civil',
            'genero',
            'cpf',
            'telefone_fixo',
            'celular',
           ]
        

class PessoaJuridicaForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})
        
    class Meta:
        model = PessoaJuridica
        fields = [
            'username', 
            'password',
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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})

    class Meta:
        model = Acessibilidade
        fields = [
            'outros_tipos_deficiencia', 
            'tipo_deficiencia', 
            'cid', 
            ]

class Avaliacao_SecretariaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})

    class Meta:
        model = Avaliacao_Secretaria
        fields = [
            'data_da_avaliacao',
            'nome_do_trabalhador',
            'telefone',
            'nome_da_empresa',
            'contratacao',
            'cargo_funcao',
            'atividade_realizada',
            'adaptacao_local_de_trabalho',
            'atencao_limitacoes_habilidades',
            'relacionamento_chefia',
            'relacionamento_colegas'
        ]
