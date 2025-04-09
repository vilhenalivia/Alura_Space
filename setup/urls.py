from django.contrib import admin
from django.urls import path, include

""" Sequência de URL'S possiveis de se atender nessa aplicação"""
urlpatterns = [
    path('admin/', admin.site.urls),
    # Acessado á galeria.urls
    path('', include('galeria.urls'))

]