from django.db import models
from django.contrib.auth.models import User
from usuarios.choices import *
from django.utils import timezone

class PessoaFisica(User):
    class Meta:
        verbose_name = 'Pessoa Física'

    nome = models.CharField(verbose_name = "Nome completo:", max_length=255, default=False)
    cpf = models.CharField(verbose_name = "CPF", max_length=14, default=False)    
    genero = models.CharField(verbose_name = "Genêro", choices= generos, max_length=255, default=False)
    estado_civil = models.CharField(verbose_name = "Estado Civil", choices=estado, max_length=255)
    data_nascimento = models.DateField(verbose_name = "Data de nascimento",max_length=10,default=False)
    telefone_fixo = models.CharField(verbose_name ="Telefone fixo", max_length=13, default=False)
    celular = models.CharField(verbose_name="Celular", max_length=13, default=False)
    ativo = models.BooleanField(default=False)
    criado_em = models.DateField(default= timezone.now, verbose_name = "Criado", max_length=255)
    

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
         
class Acessibilidade(models.Model):
    tipos_deficiencia = (
        ('FISICA', 'Fisica'),
        ('AUDITIVA', 'Auditiva'),
        ( 'Visual', (
            ('MONOCULAR','monocular'),
            ('TOTAL','total'),
            ('BAIXAVISAO','baixa visao')),),
        ('INTELECTUAL', 'Intelectual'),
        ('MULTIPLA', 'Multipla'),
        ('TEA', 'TEA'),
        ('TRANSTORNO MENTAL', 'Transtorno mental'),
        ('PSICOSOCIAL','Psicosocial'),
        ('OUTRA', 'Outra'),
    )
    outros_tipos_deficiencia = models.CharField(max_length=255,verbose_name='qual tipo?') 
    tipo_deficiencia = models.CharField(max_length=255, verbose_name='Qual sua deficiência ?',choices=tipos_deficiencia)
    cid = models.CharField(max_length=255, verbose_name='Qual o CID ?')
    protese = models.BooleanField(default=False ,verbose_name='Faz uso de alguma órtese, prótese ou meios auxiliares de locomoção? (ex: cadeira de rodas, muleta, aparelho auditivo, etc',choices=resposta)
    restricao_fisica = models.BooleanField(default=False ,verbose_name='Restrição para alguma atividade? Já teve adoecimento ou fastamento devido trabalho ou fora do trabalho? Acidente de trabalho anterior? (Demais riscos ou limitações observados pelo entrevistador)',choices=resposta)
    tecnologia = models.BooleanField(default=False ,verbose_name='Necessita de Tecnologia Assistiva para o Trabalho? Qual?',choices=resposta)

    class Meta:    
        verbose_name ='Acessibilidade'