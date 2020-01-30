from django.shortcuts import render
from vaga.forms import VagaForm

def cadastro_vaga(request):
    form = VagaForm(request.POST or None)
    args = (
        'form':form
    )
    if form.is_valid():
        form.save()
        args = (
            'msg': 'Cadastro realizado com sucesso'
        )
        return render(request, 'cadastro.html', args)
    return render(request, 'cadastro.html', args)        
