from django.db import models
from django.contrib.auth.models import User

class PessoaFisica(User):
    class Meta:
        verbose_name = 'Pessoa Física'

class PessoaJuridica(User):
    nome_fantasia = models.CharField(max_length=255, verbose_name='Nome fantasia da empresa')
    razao_social = models.CharField(max_length=255, verbose_name='Razão social da empresa')
    cnpj = models.CharField(max_length=18, verbose_name='CNPJ')
    contato_empresa = models.CharField(max_length=14, verbose_name='Contato da empresa')
    ramo_atividade = models.CharField(max_length=255, verbose_name='Ramo de atividade')
    numero_funcionarios = models.IntegerField(verbose_name='Número de funcionários')
    numero_pcds = models.IntegerField(verbose_name='Número de PCDs')

    class Meta:
        verbose_name = 'Pessoa Juridica'

class Endereco(models.Model):
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=40)
    cidade = models.CharField(max_length=40)
    estado = models.CharField(max_length=40)
    cep = models.CharField(max_length=9)

    usuario  = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:    
        verbose_name ='Endereço'
         
