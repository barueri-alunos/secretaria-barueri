from django import forms
from pessoalfisca.models import PessoaFisica

class PessoaFisicaForm(forms.ModelForm):
    class Meta:
        model = PessoaFisica
        fields = '__all__'
        
