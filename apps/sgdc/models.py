from django.db import models
from django.utils import timezone

class EspacialSegment(models.Model):
    CHOICES = [
        ('NORMAL', 'Normal'),
        ('OK', 'OK'),
        ('WARN', 'Warning'),
        ('CRIT', 'Critical'),
    ]
    SIM_NAO_CHOICES = [
        ('SIM', 'Sim'),
        ('NAO', 'Não'),
    ]

    data = models.DateField(default=timezone.now)
    plataforma_saude = models.CharField(max_length=10, choices=CHOICES)
    proc_executados = models.CharField(max_length=100, choices=CHOICES)
    alerta_conjuncao = models.CharField(max_length=100, choices=CHOICES)
    campanha_ranging = models.CharField(max_length=100, choices=CHOICES)
    prox_manobra = models.CharField(max_length=100)
    tempo_eclipse = models.DurationField()

    smc_brasilia = models.CharField(max_length=100, choices=CHOICES, verbose_name="SMC Brasília", default='OK')
    smc_rio = models.CharField(max_length=100, choices=CHOICES, verbose_name="SMC Rio", default='OK')
    cmc_brasilia = models.CharField(max_length=100, choices=CHOICES, verbose_name="CMC-x Brasília", default='OK')
    cmc_rio = models.CharField(max_length=100, choices=CHOICES, verbose_name="CMC-x Rio", default='OK')
    tcr_brasilia = models.CharField(max_length=100, choices=CHOICES, verbose_name="Antena (TCR) Brasília", default='OK')
    tcr_rio = models.CharField(max_length=100, choices=CHOICES, verbose_name="Antena (TCR) Rio", default='OK')

    enlaces_ativos = models.IntegerField(verbose_name="Enlaces Ativos", default=0)
    qualidade_enlaces = models.CharField(max_length=100, choices=CHOICES, verbose_name="Qualidade dos Enlaces", default='OK')
    antena_teatro_em_uso = models.CharField(max_length=3, choices=SIM_NAO_CHOICES, verbose_name="Antena Teatro em Uso", default='NAO')

    observacoes = models.TextField(verbose_name="Observações", blank=True, null=True)
    
    # Novos campos
    descricao_operacao = models.TextField(verbose_name="Descrição da Operação", blank=True, null=True)
    infra_critica_brasilia = models.CharField(max_length=100, choices=CHOICES, verbose_name="Infra Crítica Brasília", default='OK')
    infra_critica_rio = models.CharField(max_length=100, choices=CHOICES, verbose_name="Infra Crítica Rio de Janeiro", default='OK')
    gcn_tcr_brasilia = models.CharField(max_length=100, choices=CHOICES, verbose_name="GCN/TCR Brasília", default='OK')
    gcn_tcr_rio = models.CharField(max_length=100, choices=CHOICES, verbose_name="GCN/TCR Rio de Janeiro", default='OK')
    clima_espacial = models.CharField(max_length=100, choices=CHOICES, verbose_name="Clima Espacial", default='OK')
    ssa_sda = models.CharField(max_length=100, choices=CHOICES, verbose_name="SSA/SDA", default='OK')

    class Meta:
        unique_together = ('data',)

    def __str__(self):
        return f"{self.data} - {self.plataforma_saude} - {self.prox_manobra}"
