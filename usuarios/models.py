from django.db import models
from django.contrib.auth.models import User


class PessoaFisica(User):
    class Meta:
        verbose_name = 'Pessoa Física'

    nome = models.CharField(verbose_name = "Nome:", max_length=255)
    cpf = models.CharField(verbose_name = "CPF", max_length=14)
    generos = (
        ("ESCOLHA O GÊNERO", "Escolha o gênero"),
        ("MASCOLINO", "Mascolino"),
        ("FEMININO", "Feminino"),
        ("NÃO BINÁRIO", "Não Binário"),
        ("OUTROS", "Outros"),
    )
    genero = models.CharField(verbose_name = "Genêro", choices=generos, max_length=255, default=False)
    estado = (
        ("ESCOLHA O ESTADO CIVIL", "Escolha o estado Civil"),
        ("SOLTEIRO(A)", "Solteiro(a)"),
        ("CASADO(A)", "Casado(a)"),
        ("DIVORCIADO(A)", "Divociado(a)"),
        ("VIÙVO(A)", "Viúvo(a)")
        
    )
    estado_civil = models.CharField(verbose_name = "Estado Civil", choices=estado, max_length=255, default=True)
    data_nascimento = models.DateField(verbose_name = "Nascimento",max_length=10)
    telefones = (
        ("FIXO","Fixo"),
        ("CELULAR", "Celular"),
    )
    telefone = models.CharField(verbose_name ="Telefone", choices=telefones, max_length=13, default=True)
    telefone = models.CharField(verbose_name="Telefone", max_length=13)
    ativo = models.BooleanField(default=False)
    criado_em = models.DateField(default=timezone.now, verbose_name = "Criado", max_length=255)        

class PessoaJuridica(User):
    nome_fantasia = models.CharField(max_length=255)
    razao_social = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18)
    contato_empresa = models.CharField(max_length=14)
    ramo_ativiade = models.CharField(max_length=255)
    numero_funcionarios = models.IntegerField()
    numero_pcds = models.IntegerField()

    class Meta:
        verbose_name = 'Pessoa Juridica'