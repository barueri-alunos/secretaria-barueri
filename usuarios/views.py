from django.shortcuts import render
from usuarios.forms import *
from usuarios.models import *
# Create your views here.

def cadastrar_empresa(request):
    form = PessoaJuridicaForm(request.POST or None)
    args = {
        'form':form
    }
    if form.is_valid():
        form.save()
        args = {
            'msg': 'Cadastro realizado com sucesso'
        }
        return render(request, 'cadastro_empresa.html', args)
    return render(request, 'cadastro_empresa.html', args)

def cadastrar_pessoa_fisica(request):
    form = PessoaFisicaForm(request.POST or None)
    if form.is_valid():
        form.save()
        args = {
            'form':form,
            'msg':'O cadastro foi realizado com sucesso'
        }
        return render(request, 'cadastro.html', args)
    args = {'form':form}
    return render(request, 'cadastro.html', args)
