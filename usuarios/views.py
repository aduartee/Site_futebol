from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')

def login(request):
    return render(request, 'usuarios/login.html')

def dash(request):
    pass

def logout(request):
    pass