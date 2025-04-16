from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

""" Sequência de URL'S possiveis de se atender nessa aplicação"""
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Acessado á galeria.urls
    path('', include('galeria.urls'))

] + static(settings.MEDIA_URL, domument_root=settings.MEDIA_ROOT)