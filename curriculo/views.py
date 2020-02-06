from django.shortcuts import render
from curriculo.forms import *
from usuarios.models import PessoaFisica
from .models import *

def home(request):
    return render(request, 'base.html')

    form.save()
            
# Create your views here.
def cadastrar_competencia(request, id):
    pessoa_fisica = pessoa_fisica.objects.get(pk=id)
    form = CompetenciaForm(request.POST or None, instance=pessoa_fisica)
    args ={
            'form':form
        }
    if form.is_valid():
        form.save()
        args = {
            'msg' :'Curriculo cadastrado com sucesso!'
        }
        return render(request,'competencia.html',args)
    return  render(request, 'competencia.html',args)

def detalhes_competencias(request, id):
    competencia = PessoaFisica.objects.get(pk=id)
    form = CompetenciaForm(request.POST or None)


    args = {
        'form':form
        }
    return render(request, 'detalhe_competencias.html', args)

def atualizar_competencias(request, id):
    competencias = PessoaFisica.objects.get(pk=id)
    form = CompetenciaForm(request.POST or None,)
    
    args = {
        'form':form
        }
    
    if form.is_valid():
        form.save()
        args = {
            'msg':'Cadastro atualizado com sucesso'
        }
    return render(request, 'atualizar_competencias.html', args)

def deletar_competencias(request, id):
    competencias = Competencias.objects.get(pk=id)
    competencias.delete()

    args = {
        'msg':'O curriculo foi deletado com sucesso',
        'competencia':competencia
        }
    return render(request, 'delete_competencias.html', args)





    
        