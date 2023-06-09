from django.db import models
from datetime import datetime

# Create your models here.
class Fotografia(models.Model):
    
    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
        ("ESTRELA", "Estrela"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicado = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(null=False, blank=False, default=datetime.now)

    def __str__(self):
        return self.nome
    