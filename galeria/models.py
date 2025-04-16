from django.db import models
from datetime import datetime

# Ao alterar o models -> dar o comando makemigrations/ migration

# Create your models here.

# Classe ->Tabela pra cada fotografia
class Fotografia(models.Model):

    OPCOES_CATEGORIA =  [
        ('NEBULOSA', 'nebulosa'),
        ('ESTRELA', 'estrela'),
        ('GALAXIA', 'galaxia'),
        ('PLANETA', 'planeta')
    ]


    # Campo de caracteres com o maximo de 100 caracteres, não pode ser vazio 
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    # Campo de categoria
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA , default= '')
    # Campo de texto extenso
    descricao = models.TextField(null=False, blank=False)
    # Nome da própria foto, pode ser vazio e tem ums foto pradrao
    foto = models.ImageField(upload_to='fotos//%Y/%m/%d', blank=True)
    # Campo de verificação como publiadaou não
    publicada = models.BooleanField(default=False)
    # Data de crição de uma fotografia e p horário. Deve ter uma dado válido
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)



    #Retorna o nome do objeto criado
    def __str__(self):
        return f'Fotografia [nome = {self.nome}]'