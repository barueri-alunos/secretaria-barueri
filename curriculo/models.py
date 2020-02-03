from django.db import models
from usuarios.choices import escolaridades

# Create your models here.
class Formacao_academica(models.Model):
    class Meta:
        verbose_name = 'Formação acadêmica'
    
    escolaridade = models.CharField(max_length=128, choices= escolaridades, verbose_name='Escolaridade')
    
