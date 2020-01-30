from django.shortcuts import render
from usuarios.forms import PessoaFisicaForm
from usuarios.models import PessoaFisica

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
        




