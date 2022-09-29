from distutils.command.upload import upload
from signal import default_int_handler
from tokenize import blank_re
from django.db import models
from datetime import datetime
from statistics import mode
from pessoas.models import Pessoa

class Futebol(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_time = models.CharField(max_length=200)
    informacoes = models.TextField()
    ano_criacao = models.TextField()
    numero_titulos = models.IntegerField()
    historio = models.CharField(max_length=100)
    divisao = models.CharField(max_length=50)
    foto_time = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)
    ano_criacao = models.DateTimeField(default=datetime.now, blank=True)
    publicacao = models.BooleanField(default=False, )

    def __str__(self):
        return self.nome_time