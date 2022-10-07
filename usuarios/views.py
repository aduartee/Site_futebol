from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import user

def cadastro(request):
    if request.method == 'POST':
        name = request.POST('nome')
        email = request.POST('email')
        senha = request.POST('password')
        senha2 = request.POST('password2')
        if not name.strip():
            print('Nome não pode ficar em branco')
            return redirect('cadastro')
        
        if not email.strip('Email não pode fica vazio'):
            return redirect('cadastro')
        
        if senha != senha2: 
            print('Senhas devem ser iguais')
            return redirect('cadastro')
        
        if 
        print('Usuario cadastrado com sucesso: ', name, email, senha, senha2 )
        
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    return render(request, 'usuarios/login.html')

def dash(request):
    pass

def logout(request):
    pass