from django.db import models
from django.utils import timezone

class ContratosImagens(models.Model):
    data = models.DateField('Data', default=timezone.now)
    lote_7_planejado = models.IntegerField('Lote 7 Planejado')
    iceye_planejado = models.IntegerField('ICEYE Planejado')
    lote_7_recebido = models.IntegerField('Lote 7 Recebido')
    iceye_recebido = models.IntegerField('ICEYE Recebido')

    def __str__(self):
        return f"Contrato de Imagens - {self.data}"
