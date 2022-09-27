from http.client import HTTPResponse
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

