from django.contrib import admin
from galeria.models import Fotografia


class ListandoFotografias(admin.ModelAdmin):
    # Mostrar o ID o Nome e a Legenda no display
    list_display = ('id', 'nome', 'legenda', 'publicada')
    
    # Mostrar o display dos links - Quais informações vão ser links
    list_display_links=('id', 'nome')
    
    # Área de busca pleo nome 
    search_fields = ('nome',)   # Deve ser tupla

    # Listar por categoria
    list_filter = ('categoria', ) # Deve ser tupla

    # Itens por pagina
    list_per_page = 10

    # Alterar o valor de "publicada"
    list_editable = ('publicada',) # Deve ser uma tupla

# Registro de informações na area de administração
admin.site.register(Fotografia, ListandoFotografias)


