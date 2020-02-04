from django.shortcuts import render
from curriculo.forms import *
from curriculo.models import *

# Create your views here.
def cadastrar_competencia(request):
    form = CompetenciaForm(request.POST or None)
    args ={
            'form':form,
        }
    if form.is_valid():
        form.save()
        args['msg'] = 'Curriculo cadatrado com sucesso!'
        return render(request,'competencia.html',args)
    return  render(request, 'competencia.html',args)   
        