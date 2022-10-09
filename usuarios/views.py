from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth

def cadastro(request):
    if request.method == 'POST':
        name = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if not name.strip():
            print('Nome não pode ficar em branco')
            return redirect('cadastro')
        
        if not email.strip:
            print('Email não pode fica vazio')
            return redirect('cadastro')
        
        if senha != senha2: 
            print('Senhas devem ser iguais')
            return redirect('cadastro')
        
        if User.objects.filter(email=email).exists():
            print ('Usuario já cadastrado')
            return redirect('cadastro')
        
        user = User.objects.create_user(username=name, email=email,password=senha)
        user.save()
        print('Usuario cadastrado com sucesso: ', name, email, senha, senha2 )
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == '' or senha == '': 
            print('Usuario não podem estar vazios')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None: 
                auth.login(request, user)
                return redirect('dashboard')
                
        return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html')
    else:
        return render('index')


def logout(request):
    auth.logout(request)
    return redirect('index') 

def cria(request):
    return render(request, 'usuarios/criar.html')
 
