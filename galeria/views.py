""" Cuidar do que sera visível na tela"""
from django.shortcuts import render
from galeria.models import Fotografia

""" Resposta para a requisição"""
def index(request):
  
    # Busca os itens do banco de dados que estão marcados como publicadas em ordem de mais recente primeiro.
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada = True)

    """ Retorna a request e a pagina html de templates"""
    return render(request, 'galeria/index.html', {"cards": fotografias})
    
def imagem(request):
    return render(request, 'galeria/imagem.html')