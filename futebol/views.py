from http.client import HTTPResponse
import re
from tracemalloc import get_object_traceback
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Futebol

def index(request):
    
    futebol = Futebol.objects.order_by('ano_criacao').filter(publicacao=True)
        
    dados = {
       'futebol' : futebol
    }
    return render(request, 'index.html',  dados)

def receita(request, futebol_id):
    futebol = get_object_or_404(Futebol, pk=futebol_id)
    
    time_a_exibir = {
        'futebol' : futebol
    }
    return render(request, 'receita.html', time_a_exibir)

def buscar(request):
    lista_times = Futebol.objects.order_by('-ano_criacao').filter(publicacao=True)
    
    if 'buscar' in request.GET:
        nome_busca = request.GET['buscar']
        if buscar:
            lista_times = lista_times.filter(nome_time__icontains=nome_busca)
        
    dados = {
        'futebol' : lista_times
    }
    return render(request, 'buscar.html', dados)