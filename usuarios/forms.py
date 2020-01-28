from django import forms
from usuarios.models import PessoaFisica

class PessoaFisicaForm(forms.ModelForm):
    class Meta:
        model = PessoaFisica
        fields = '__all__'
        
