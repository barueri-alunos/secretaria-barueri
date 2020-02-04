from django.shortcuts import render
from curriculo.forms import *
from curriculo.models import *

# Create your views here.
def competencia(request):
    form = CompetenciaForm(request.POST or None)

    if form.is_valid():
        form.save()
        args ={
            'form':form,
            'msg':'Curriculo cadatrado com sucesso!'
        }
        return render(request,'competencia.html',args)
    args ={'form':form}
    return render(request,'competencia.html',args)