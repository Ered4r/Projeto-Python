from django.shortcuts import render, redirect
from .forms import PessoaForm
from .models import Pessoa


def criar_pessoa(request):
    existing_usernames = Pessoa.objects.values_list('username', flat=True)
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    else:
        form = PessoaForm()
    return render(request, 'login/criar_pessoa.html', {'form': form, 'existing_usernames': existing_usernames})        


def listar_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'login/listar_pessoas.html', {'pessoas': pessoas})
# Create your views here.
