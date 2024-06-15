from django.db import models
from django.utils import timezone

class EspacialSegment(models.Model):
    CHOICES = [
        ('OK', 'OK'),
        ('WARN', 'Warning'),
        ('CRIT', 'Critical'),
    ]
    SIM_NAO_CHOICES = [
        ('SIM', 'Sim'),
        ('NAO', 'Não'),
    ]

    data = models.DateField(default=timezone.now)  # Data do briefing
    plataforma_saude = models.CharField(max_length=10, choices=CHOICES)  # Saúde da plataforma
    proc_executados = models.CharField(max_length=100, choices=CHOICES)  # Processos executados
    alerta_conjuncao = models.CharField(max_length=100, choices=CHOICES)  # Alerta de conjunção
    campanha_ranging = models.CharField(max_length=100, choices=CHOICES)  # Campanha de ranging
    prox_manobra = models.CharField(max_length=100)  # Próxima manobra
    tempo_eclipse = models.DurationField()  # Tempo em eclipse

    smc_brasilia = models.CharField(max_length=100, choices=CHOICES, verbose_name="SMC Brasília", default='OK')
    smc_rio = models.CharField(max_length=100, choices=CHOICES, verbose_name="SMC Rio", default='OK')
    cmc_brasilia = models.CharField(max_length=100, choices=CHOICES, verbose_name="CMC-x Brasília", default='OK')
    cmc_rio = models.CharField(max_length=100, choices=CHOICES, verbose_name="CMC-x Rio", default='OK')
    tcr_brasilia = models.CharField(max_length=100, choices=CHOICES, verbose_name="Antena (TCR) Brasília", default='OK')
    tcr_rio = models.CharField(max_length=100, choices=CHOICES, verbose_name="Antena (TCR) Rio", default='OK')

    enlaces_ativos = models.IntegerField(verbose_name="Enlaces Ativos", default=0)
    qualidade_enlaces = models.CharField(max_length=100, choices=CHOICES, verbose_name="Qualidade dos Enlaces", default='OK')
    antena_teatro_em_uso = models.CharField(max_length=3, choices=SIM_NAO_CHOICES, verbose_name="Antena Teatro em Uso", default='NAO')

    class Meta:
        unique_together = ('data',)

    def __str__(self):
        return f"{self.data} - {self.plataforma_saude} - {self.prox_manobra}"
