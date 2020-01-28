from django.db import models
from django.contrib.auth.models import User



class PessoaFisica(User):
    class Meta:
        verbose_name = 'Pessoa Física'

class PessoaJuridica(User):
    nome_fantasia = models.CharField(max_length=255)
    razao_social = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18)
    contato_empresa = models.CharField(max_length=14)
    ramo_atividade = models.CharField(max_length=255)
    numero_funcionarios = models.IntegerField()
    numero_pcds = models.IntegerField()

    class Meta:
        verbose_name = 'Pessoa Juridica'