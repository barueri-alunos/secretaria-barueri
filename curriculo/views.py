from django.shortcuts import render
from curriculo.forms import * 
from curriculo.models import *
from usuarios.models import *


# Create your views here.
def cadastrar_competencia(request):
    form = CompetenciaForm(request.POST or None)
    args ={
            'form':form,
        }
    if form.is_valid():
        form.save()
        args['msg'] = 'Curriculo cadatrado com sucesso!'
        return render(request,'competencia.html',args)
    return  render(request, 'competencia.html',args)

def detalhes_competencia(request, id):
    competencia = PessoaFisica.objects.get(pk=id)
    form = CompetenciaForm(request.POST or None)
    args = {
        'form':form,
        }
    return render(request, 'detalhes_competencia.html', args)

def atualizar_competencia(request, id):
    gd = PessoaFisica.objects.get( pk=id)
    form = CompetenciaForm(request.POST or None)
    args = {
        'form':form,
        }
    return render(request, 'atualizar_competencia.html', args)


def deletar_competencia(request, id):
    dcpf = PessoaFisica.objects.get(pk=id)
    form = CompetenciaForm(request.POST or None)
    args = {
        'form':form,
    }
    return render(request, 'deletar_competencia.html', args)