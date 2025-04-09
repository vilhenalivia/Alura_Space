from django.urls import path
from galeria.views import index

urlpatterns = [
    # Endereço home da aplicação
    path('', index)
]