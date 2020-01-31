from django.shortcuts import render
from vaga.forms import VagaForm
from .models import *


def cadastro_vaga(request):
    vagas = VagaForm(request.POST or None)
    args = {
        'vagas':vagas
    }
    if form.is_valid():
        form.save()
        args = {
            'msg': 'Cadastro realizado com sucesso'
        }
        return render(request, 'cadastro.html', args)
    return render(request, 'cadastro.html', args)        

def editar_vagas(request):
    vagas = Vaga.objects.get(pk=id)
    form = VagaForm(request.POST or None, instance=vagas)
    args = {
        'form':form
    }
    if form.is_valid():
        form.save()
        args = {
            'msg': 'Informações da vaga atualizadas'
        }
    return render(request, 'editar_vagas.html', args)

def detalhe_vaga(request, id):
    vaga = Vaga.objects.get(pk=id)
    args = {
        'vaga':vaga
    }
    return render(request, 'detalhe_vagas.html', args)

def remover_vaga(request, id):
    vaga = Vaga.objects.get(pk=id)
    vaga.delete()

    args = {
        'msg': 'Vaga deletada com sucesso',
        'vaga':vaga
    }
    return render(request, 'detalhe_vagas.html', args)