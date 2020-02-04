from django.shortcuts import render
from curriculo.forms import *
from curriculo.models import *

# Create your views here.
def cadastrar_competencia(request, id):
    pff = PessoaFisica.objects.get(pk=id)
    form = CompetenciaForm(request.POST or None, instance=pff)
    args ={
            'pff':pff,
        }
    if form.is_valid():
        form.save()
        args['msg'] = 'Curriculo cadatrado com sucesso!'
        return render(request,'competencia.html',args)
        curricu = form.save(commit=False)
        seu_curricu = PessoaFisica
        curricu.save()
    return  render(request, 'competencia.html',args)



    
        