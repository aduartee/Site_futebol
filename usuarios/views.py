from contextlib import redirect_stderr
from time import time
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth, messages
from futebol.models import Futebol



def cadastro(request):
    if request.method == 'POST':
        name = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        
        if campo_vazio(name):
            messages.error(request, 'Nome não pode ficar em branco') 
            return redirect('cadastro')
        
        if campo_vazio(email):
            messages.error(request, 'Email não pode ficar vazio')
            return redirect('cadastro')
        
        if campo_diferente(senha, senha2): 
            messages.error(request, 'As senhas devem ser iguais!!')
            return redirect('cadastro')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuario já cadastrado')
            return redirect('cadastro')
        
        if User.objects.filter(username=name).exists():
            messages.error(request, 'Usuario já cadastrado')
            return redirect('cadastro')
        
        user = User.objects.create_user(username=name, email=email,password=senha)
        user.save()
        messages.success(request, 'Usuario cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == '' or senha == '': 
            messages.error(request,'Usuario e senha não podem estar vazios')
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
        id = request.user.id
        times = Futebol.objects.order_by('-ano_criacao').filter(pessoa=id)
        
        dados = {
            'futebol' : times
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')  


def logout(request):
    auth.logout(request)
    return redirect('index') 

def cria(request):
    if request.method == 'POST':
        nome_time = request.POST['nome_time']
        historia = request.POST['historio']
        informacoes = request.POST['informacoes']
        ano_criacao = request.POST['ano_criacao']
        numero_titulos = request.POST['numero_titulos']
        divisao = request.POST['divisao']
        foto_time = request.FILES['foto_time']
        user = get_object_or_404(User, pk=request.user.id)
        time = Futebol.objects.create(pessoa=user, nome_time=nome_time, historio=historia, informacoes=informacoes, ano_criacao=ano_criacao, numero_titulos=numero_titulos
                                      ,divisao=divisao, foto_time=foto_time)
        time.save()
        return redirect('dashboard')
    else:
       return render(request, 'usuarios/criar.html')


def campo_vazio(campo):
    return not campo.strip()
    
def campo_diferente(campo1, campo2):
    return campo1 != campo2