from django.shortcuts import render
from pessoafisisca.forms import pessoafisiscaForm
from pessoafisica.models import pessoafisica

def cadastrar_pessoa_fisica(request):
    form = PessoaFisicaForm(request.POST or None)
    if form.is_valid():
        form.save()
        args = {
             'form': form, 
             'msg': 'Cadastro foi realizado com sucesso!'
        }
        render(request, 'cadastro.html', args)
        args = {'form': form}
        return render('request.cadastro.html', args)
        args = {form'form'}


''


