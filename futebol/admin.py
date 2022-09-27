from django.contrib import admin
from .models import Futebol

class Listando_times(admin.ModelAdmin):
    list_display = ('id', 'nome_time', 'numero_titulos', 'publicacao')
    list_display_links = ('id', 'nome_time')
    search_fields = ('nome_time',)
    list_per_page = 5
    list_editable = ('publicacao', )
    
    
admin.site.register(Futebol, Listando_times)
