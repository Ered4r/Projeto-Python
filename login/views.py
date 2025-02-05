from django.shortcuts import render, redirect
from .forms import PessoaForm
from .models import Pessoa
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.http import HttpResponse

@login_required
def home(request):
    return render(request, 'login/home.html')

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

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after login
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'registration/login.html')