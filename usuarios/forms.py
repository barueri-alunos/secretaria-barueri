from django import forms
from usuarios.models import PessoaFisica

class PessoaFisicaForm(forms.ModelForm):
    class Meta:
        model = PessoaFisica
        fields = [ 'first_name', 'last_name', 'username', 'password']
        
