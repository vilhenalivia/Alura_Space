""" Cuidar do que sera visível na tela"""
from django.shortcuts import render


""" Resposta para a requisição"""
def index(request):
    """ Retorna a request e a pagina html de templates"""
    return render(request, 'galeria/index.html')
    