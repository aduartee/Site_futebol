from pydoc import ModuleScanner
from re import search
from django.contrib import admin
from . models import Pessoa

class mostra_pessoa(admin.ModelAdmin):
    list_display = ('id','nome','email')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_per_page = 10
    
admin.site.register(Pessoa, mostra_pessoa)
