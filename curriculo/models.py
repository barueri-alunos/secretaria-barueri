from django.db import models
from curriculo.choices import *
from django.utils import timezone
from usuarios.models import PessoaFisica
import datetime

# Create your models here.
class Competencia(models.Model):
    class Meta:
        verbose_name = 'Competência'
    
    pessoa  = models.ForeignKey(PessoaFisica,on_delete=models.CASCADE)
    objetivo = models.CharField(max_length=255, verbose_name='Objetivos')
    qualificacao_profissional = models.CharField(verbose_name='Qualificação Profissional', max_length=255, null=True)
    pretensao_salarial = models.DecimalField(max_digits=10, decimal_places=2)
    escolaridade = models.CharField(max_length=128, choices=escolaridades, verbose_name='Escolaridade')
    curso = models.CharField(max_length=100, verbose_name='Qual o curso')
    instituicao_ensino = models.CharField(max_length=255, verbose_name='Instituição que realizou o curso')
    ano_inicio = models.DateField(verbose_name='Ano de inicio')
    ano_termino = models.DateField(verbose_name='Ano de termino')
    cursos_extras = models.CharField(max_length=255, verbose_name='Cursos extras')
    nivel_de_leitura = models.CharField(max_length=100, choices=leitura, verbose_name='Nivel de leitura')
    nivel_informatica = models.CharField(max_length=255)
    word_nivel = models.CharField(max_length=100, choices=leitura, verbose_name='Word')
    excel_nivel = models.CharField(max_length=100, choices=excel, verbose_name='Excel')
    pptx_nivel = models.CharField(max_length=100, choices=power_point, verbose_name='Power Point')
    internet_nivel = models.CharField(max_length=100, choices=internet, verbose_name='Internet')
    lingua = models.CharField(max_length=255, verbose_name='Linguas estrangeiras')

    def __str__(self):
        return self.objetivo








    
