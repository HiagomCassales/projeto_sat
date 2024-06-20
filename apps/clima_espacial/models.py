from django.db import models
from django.utils import timezone

class ClimaEspacial(models.Model):
    SIM_NAO_CHOICES = [
        ('Sim', 'Sim'),
        ('Não', 'Não')
    ]
    
    data = models.DateField('Data', default=timezone.now)
    maior_k_24h = models.FloatField('Maior K nas últimas 24h')
    maior_k_previsto = models.FloatField('Maior K previsto até D+2')
    tempestade_solar_prevista = models.CharField('Tempestade Solar Prevista', max_length=3, choices=SIM_NAO_CHOICES)

    def __str__(self):
        return f'Maior K 24h: {self.maior_k_24h}, Previsto: {self.maior_k_previsto}'
