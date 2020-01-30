from django.db import models
from usuarios.models import PessoaJuridica
from vaga.choices import *

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


class Detalhes(models.Model):
    conhecimento_tecnico = models.CharField(max_length=255, verbose_name='Conhecimentos técnicos')
    conhecimento_informatica = models.CharField(max_length=100, verbose_name='Conhecimento em informatica')
    carregar_peso = models.BooleanField(default=False, verbose_name='Carregará peso ?', choices=resposta)
    peso = models.CharField(max_length=128, verbose_name='Quantos kgs em média?')
    uso_escada = models.BooleanField(default=False, verbose_name='Fará uso constante da escada ?', choices=resposta)
    uso_elevador = models.BooleanField(default=False, verbose_name='Há elevador ou acessibilidade para modalidade ?', choices=resposta)
    tipo_atendimento = models.BooleanField(default=False, verbose_name='Há necessidade de atendimento ao público/cliente ? ',choices=resposta)
    postura_principal = models.CharField(max_length=255, default=False ,choices=posturas_principal, verbose_name='Qual forma de comunicação principal ?')
    decisoes_complexas = models.BooleanField(default=False, verbose_name='Atividade exige concentração e tomadas de decisões complexas ?', choices=resposta)
    uso_ferramentas = models.CharField(max_length=255, verbose_name='Quais ferramentas ou equipamentos serão utilizados na atividade?')
    uso_epi = models.CharField(max_length=255, verbose_name='Fará uso de EPI (Equipamento de Proteção Individual: Bota, protetor auricular, óculos de proteção, ect)? Quais ?')
    acessibilidades = models.CharField(max_length=255, verbose_name='Quais recursos de acessibilidade empresa dispõe?')
    adaptacoes = models.CharField(max_length=255, verbose_name='Há necessidade de apoio para adaptações para acessibilidade?')
    data_entrevista = models.DateField(verbose_name= 'Data Prevista', default=datetime.date.today, auto_now=False, auto_now_add=False)
    local_entrevista = models.CharField(max_length=255, verbose_name='Local da Entrevista')
    termino_selecao = models.CharField(max_length=255, verbose_name='Previsão de término do processo seletivo')

    def __str__(self):
        return self.termino_selecao