from django.shortcuts import render
from curriculo.forms import *
from usuarios.models import PessoaFisica
from .models import *

# Create your views here.
def cadastrar_competencia(request, id):
    competencia = Competencia.objects.get(pk=id)
    form = CompetenciaForm(request.POST or None, instance=pessoa_fisica)
    args ={
            'form':form
        }
    if form.is_valid():
        form.save()
        args = {
            'msg' :'Curriculo cadatrado com sucesso!'
        }
        return render(request,'cadastrar_competencia.html',args)
    return  render(request, 'cadastrar_competencia.html',args)



    
        