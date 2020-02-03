from django import forms
from models import *

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = [
            'objetivo',
            'qualificacao_profissional',
            'pretencao_salarial',
            'escolaridade',
            'qual_curso',
            'instituicao_ensino_curso',
            'ano_inicio',
            'ano_termino',
            'cursos_extras',
            'nivel_de_leitura',
            'nivel_informatica',
            'lingua_estrangeira',
            'lingua',
        ]