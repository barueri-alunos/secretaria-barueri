from django.db import models
from django.contrib.auth.models import User
from usuarios.choices import *
from django.utils import timezone

class PessoaFisica(User):
    class Meta:
        verbose_name = 'Pessoa Física'

    nome = models.CharField(verbose_name = "Nome completo:", max_length=255, null=True)
    cpf = models.CharField(verbose_name = "CPF", max_length=25, unique=True, null=True)    
    genero = models.CharField(verbose_name = "Gênero", choices=generos, max_length=25, null=True)
    estado_civil = models.CharField(verbose_name = "Estado Civil", choices=estado, max_length=255, null=True)
    data_nascimento = models.DateField(verbose_name = "Data de nascimento", null=True)
    telefone_fixo = models.CharField(verbose_name ="Telefone fixo", max_length=25, null=True, blank=True)
    celular = models.CharField(verbose_name="Celular", max_length=25, null=True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateField(default= timezone.now, verbose_name = "Criado em")
    

class PessoaJuridica(User):
    class Meta:
        verbose_name = 'Pessoa Juridica'
        
    nome_fantasia = models.CharField(max_length=255, verbose_name='Nome fantasia da empresa', null=True)
    razao_social = models.CharField(max_length=255, verbose_name='Razão social da empresa', null=True, blank=True)
    cnpj = models.CharField(max_length=18, verbose_name='CNPJ', null=True, blank=True)
    contato_empresa = models.CharField(max_length=128, verbose_name='Contato da empresa', null=True, blank=True)
    ramo_atividade = models.CharField(max_length=255, verbose_name='Ramo de atividade', null=True, blank=True)
    numero_funcionarios = models.IntegerField(verbose_name='Número de funcionários', null=True, blank=True)
    numero_pcds = models.IntegerField(verbose_name='Número de PCDs', null=True, blank=True)


class Endereco(models.Model):
    class Meta:    
        verbose_name ='Endereço'
        
    logradouro = models.CharField(max_length=128, null=True, blank=True, verbose_name='Endereço:')
    numero = models.CharField(max_length=128, null=True, blank=True, verbose_name='Número')
    complemento = models.CharField(max_length=128, null=True, blank=True, verbose_name='Complemento')
    cidade = models.CharField(max_length=128, verbose_name='Cidade')
    estado = models.CharField(max_length=128, choices=estados, verbose_name='Estado')
    cep = models.CharField(max_length=20, verbose_name='CEP')
    usuario  = models.ForeignKey(User,on_delete=models.CASCADE)

         
class Acessibilidade(models.Model):
    class Meta:    
        verbose_name ='Acessibilidade'

    outros_tipos_deficiencia = models.CharField(max_length=255,verbose_name='qual tipo?') 
    tipo_deficiencia = models.CharField(max_length=255, verbose_name='Qual sua deficiência ?',choices=tipos_deficiencia)
    cid = models.CharField(max_length=255, verbose_name='Qual o CID ?')
    protese = models.BooleanField(default=False ,verbose_name='Faz uso de alguma órtese, prótese ou meios auxiliares de locomoção? (ex: cadeira de rodas, muleta, aparelho auditivo, etc',choices=resposta)
    restricao_fisica = models.BooleanField(default=False ,verbose_name='Restrição para alguma atividade? Já teve adoecimento ou fastamento devido trabalho ou fora do trabalho? Acidente de trabalho anterior? (Demais riscos ou limitações observados pelo entrevistador)',choices=resposta)
    tecnologia = models.BooleanField(default=False ,verbose_name='Necessita de Tecnologia Assistiva para o Trabalho? Qual?',choices=resposta)

