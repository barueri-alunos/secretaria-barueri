from django.shortcuts import render
from usuarios.forms import *
from usuarios.models import *
# Create your views here.

def home(request):
    return render(request, 'base.html')

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
        return render(request, 'cadastro_pj.html', args)
    return render(request, 'cadastro_pj.html', args)

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

def detalhes_pessoa_fisica(request):
    pf= PessoaFisica.objects.filter().all()
    args = {'pessoafisica': pessoafisisca}
    return render(request, 'detalhes.html', args)

def atualizar_pessoa_fisica(request, id):
    pf = pessoafisica.objects.get(pk = id)
    form = PessoaFisicaForm(request.POST or None, instance = pf)

    args = {'form': form}

    if form.is_valid():
        form.save()
        args = {'msg': 'Cadastro atualizado com sucesso'}
        return render(request, 'atualizarpf.html', args)

def deletar_pessoa_fisica(request, id):
    pf = pessoafisica.objects.get(pk = id)
    form = PessoaFisicaForm(request.POST or None, instance = pf)

    args = {'form': form}

    if form.is_valid():
        form.save()
        args = {'msg': 'Cadastro deletaado com sucesso'}
        return render(request, 'delitepf.html', args)



def acessibilidade_cadastro(request): 

    form = AcessibilidadeForm(request.POST or None)

    if form.is_valid():
        form.save()
        args ={
            'form':form,
            'msg':'O cadastro foi realizado com sucesso'

        }
        return render(request,'acessibilidade.html',args)
    args ={'form':form}
    return render(request,'acessibilidade.html',args)
