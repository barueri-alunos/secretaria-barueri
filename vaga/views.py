from django.shortcuts import render, redirect
from vaga.forms import VagaForm
from usuarios.models import PessoaJuridica
from .models import * 


def cadastro_vaga(request, id):
    form = VagaForm(request.POST or None)
    
    args = {
        'form': form
    }

    if form.is_valid():
        try:
            pessoa_juridica = PessoaJuridica.objects.get(pk=id)
        except:
            args = {
                'msg': 'pessoa juridica nao existe'
            }
            return render(request, 'cadastro_vagas.html', args)

        vaga = form.save(commit=False)
        vaga.empresa = pessoa_juridica
        vaga.save()
        
        return redirect(f'/dados/pj/detalhes/{pessoa_juridica.id}')
    return render(request, 'cadastro.html', args)        

#essa página vai editar uma vaga
def editar_vagas(request, id):
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
    return render(request, 'editar_vagas.html', args)


#essa página vai listar as vagas
def lista_vaga(request):
    vagas = Vaga.objects.filter(ativo=True).all()
    args = {
        'vagas':vagas
    }
    return render(request, 'lista_vagas.html', args)


def remover_vaga(request, id):
    vaga = Vaga.objects.get(pk=id)
    if vaga is not None:
        vaga.ativo = False
        vaga.save()
    return render(request, 'detalhe_vagas.html', {'msg' : 'Ops, deu ruim'})

def detalhe_vaga(request, id):
    vagas = Vaga.objects.get(pk=id)
    detalhes = vagas.detalhes_set.all().filter(ativo=True)
    args ={
        'vaga':vaga
    }
    return render(request, 'detalhe_vagas.html', args)

