from django import forms
from .models import *

class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = '__all__'
        