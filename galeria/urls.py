from django.urls import path
from galeria.views import index, imagem


urlpatterns = [
    # Endereço home da aplicação
    path('', index, name='index' ),
    path('imagem/', imagem, name='imagem')
]