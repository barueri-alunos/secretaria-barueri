from django.db import models
from django.contrib.auth.models import User


class PessoaFisica(User):
<<<<<<< HEAD
=======
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
    # email = models.EmailField(verbose_name="E-mail")
    ativo = models.BooleanField(default=False)
    criado_em = models.DateField(default=timezone.now, verbose_name = "Criado", max_length=255)
    tipos_de_deficiencia=(
        ("FISICA", "Fisica"),
        ("CADERANTE","Cadderante"),
        ("AUDITIVA","Auditiva"),
        ("VISUAL","Visual"),
        ("INTELECTUAL","Itelectual"),
        ("MULTIPLA","Mutipla"),
        ("TEA", "Tea"),
        ("TRANSTORNO MENTAL","Trasntorno Mental"),
        ("OUTOS","Outros"),
    )
    tipo_de_deficiencia = models.CharField(verbose_name="Restirões",choices=tipos_de_deficiencia, max_length=255, default=True)
    outros = models.CharField(verbose_name="Outros", max_length=255, default=True)
    cid = models.CharField(verbose_name="CID",max_length=150, )
    recursos = (
        ('sim', 'sim'),
        ('nao', 'nao'),
    )
    recurso = models.CharField(verbose_name="Restrições",max_length=255, choices=recursos, default=True)
    observacao_recurso = models.CharField(verbose_name="Observação do recurso", max_length = 255, default=True)
    tecnologia_assistiva = models.BooleanField(verbose_name="Você precisa de Tecnologia Assistiva?",default=False)
    tecnologia_assistiva = models.CharField(max_length=255)
    transporte_mobilidade = models.BooleanField(verbose_name="Transporte",default=False)
    transporte_mobilidade = models.CharField(max_length=255)
    automovel_proprio = models.BooleanField(verbose_name="Automovel",default=False)
    automovel_proprio = models.CharField(max_length=255)
    recursos_financeiros = models.BooleanField(verbose_name="Financeiro", default=False)
    recursos_financeiros = models.CharField(max_length=255)
    
>>>>>>> 24ea8f7... Corrigir erros de escritas da models
    class Meta:
        verbose_name = 'Pessoa Física'

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