from django.db import models
from django.contrib.auth.models import User


class PessoaFisica(User):
    class Meta:
        verbose_name = 'Pessoa Física'
