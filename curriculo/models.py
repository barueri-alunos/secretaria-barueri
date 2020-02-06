from django.db import models
from curriculo.choices import *
from django.utils import timezone
import datetime
from usuarios.models import PessoaFisica

# Create your models here.
class Competencia(models.Model):
    class Meta:
        verbose_name = 'Competência'
    
    objetivo = models.CharField(max_length=255, verbose_name='Objetivos')
    qualificacao_profissional = models.CharField(verbose_name='Qualificação Profissional', max_length=255, null=True)
    pretencao_salarial = models.DecimalField(max_digits=10, decimal_places=2)
    escolaridade = models.CharField(max_length=128, choices=escolaridades, verbose_name='Escolaridade')
    qual_curso = models.CharField(max_length=100, verbose_name='Qual o curso')
    instituicao_ensino_curso = models.CharField(max_length=255, verbose_name='Instituição que realizou o curso')
    ano_inicio = models.DateField(verbose_name='Ano de inicio')
    ano_termino = models.DateField(verbose_name='Ano de termino')
    cursos_extras = models.CharField(max_length=255, verbose_name='Cursos extras')
    nivel_de_leitura = models.CharField(max_length=100, choices=leitura, verbose_name='Nivel de leitura')
    nivel_informatica = models.CharField(max_length=100, choices=informatica, verbose_name='Nivel de informatica')
    lingua_estrangeira = models.BooleanField(verbose_name='Lingua Estrangeira')
    lingua = models.TextField()
    pessoa_fisica = models.ForeignKey(PessoaFisica, on_delete=models.CASCADE, verbose_name='Pessoa fisica')


    def __str__(self):
        return self.objetivo








    
