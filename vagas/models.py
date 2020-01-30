from django.db import models
from usuarios.models import PessoaJuridica
from vagas.choices import *

class Vaga(models.Model):
    titulo_vaga = models.CharField(max_length=255, verbose_name='Título da vaga')
    responsavel_vaga = models.CharField(max_length=255, verbose_name='Responsável pela vaga')
    contato_secretaria = models.CharField(max_length=255, verbose_name='Contato da Secretaria')
    area_vaga = models.CharField(max_length=255, verbose_name='Área da vaga')
    telefone = models.CharField(max_length=16, verbose_name='Telefone')
    quantidade_vagas = models.IntegerField(verbose_name='Quantidade de Vagas')
    salario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Salário')
    dias_trabalho = models.CharField(max_length=100)
    horario_inicio = models.TimeField(verbose_name='Horário de início')
    horario_final = models.TimeField(verbose_name='Horário de término')
    beneficios = models.CharField(max_length=255, verbose_name='Quais os benefícios')
    escolaridade = models.CharField(max_length=6, choices=escolaridade_minima, verbose_name='Escolaridade mínima' )
    data_abertura = models.DateField(verbose_name='Data de abertura da vaga')
    detalhes = models.TextField(verbose_name='Detalhes sobre a vaga')
    empresa = models.ForeignKey(PessoaJuridica, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo_vaga