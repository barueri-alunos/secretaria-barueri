from django import forms
from usuarios.models import PessoaJuridica

class PessoaJuridicaForm(forms.ModelForm):
    class Meta:
        model = PessoaJuridica
        fields = '__all__'