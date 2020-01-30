from django import forms
from vaga.models import Vaga

class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = '__all__'



