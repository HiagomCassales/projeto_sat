# briefing_raoa_sgdc/models.py

from django.db import models
from django.utils import timezone

class BriefingRaoa(models.Model):
    CHOICES = [
        ('NORMAL', 'Normal'),
        ('OK', 'OK'),
        ('WARN', 'Warning'),
        ('CRIT', 'Critical'),
    ]

    data = models.DateField(default=timezone.now)
    descricao_operacao = models.TextField(verbose_name="Descrição da Operação", blank=True, null=True)
    infra_critica_brasilia = models.CharField(max_length=100, choices=CHOICES, verbose_name="Infra Crítica Brasília", default='OK')
    infra_critica_rio = models.CharField(max_length=100, choices=CHOICES, verbose_name="Infra Crítica Rio de Janeiro", default='OK')
    gcn_tcr_brasilia = models.CharField(max_length=100, choices=CHOICES, verbose_name="GCN/TCR Brasília", default='OK')
    gcn_tcr_rio = models.CharField(max_length=100, choices=CHOICES, verbose_name="GCN/TCR Rio de Janeiro", default='OK')
    clima_espacial = models.CharField(max_length=100, choices=CHOICES, verbose_name="Clima Espacial", default='OK')
    ssa_sda = models.CharField(max_length=100, choices=CHOICES, verbose_name="SSA/SDA", default='OK')

    def __str__(self):
        return f"{self.descricao_operacao[:50]} - {self.infra_critica_brasilia} - {self.infra_critica_rio}"
