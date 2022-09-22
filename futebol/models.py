from signal import default_int_handler
from django.db import models
from datetime import datetime
from statistics import mode

class Futebol(models.Model):
    nome_time = models.CharField(max_length=200)
    informacoes = models.TextField()
    ano_criacao = models.TextField()
    numero_titulos = models.IntegerField()
    historio = models.CharField(max_length=100)
    divisao = models.CharField(max_length=50)
    ano_criacao = models.DateTimeField(default=datetime.now, blank=True)
