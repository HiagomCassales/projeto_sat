from django.db import models
from django.utils import timezone

class Lessonia(models.Model):
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

    data = models.DateField(default=timezone.now, verbose_name="Data")

    # Saúde da plataforma
    saude_plataforma_x18 = models.CharField(max_length=10, choices=CHOICES, verbose_name="Saúde da Plataforma X18")
    saude_plataforma_x19 = models.CharField(max_length=10, choices=CHOICES, verbose_name="Saúde da Plataforma X19")

    # Alerta de Conjunção
    alerta_conjuncao_x18 = models.CharField(max_length=10, choices=CHOICES, verbose_name="Alerta de Conjunção X18")
    alerta_conjuncao_x19 = models.CharField(max_length=10, choices=CHOICES, verbose_name="Alerta de Conjunção X19")

    # Manobra
    manobra_x18 = models.CharField(max_length=3, choices=SIM_NAO_CHOICES, verbose_name="Manobra X18")
    manobra_x19 = models.CharField(max_length=3, choices=SIM_NAO_CHOICES, verbose_name="Manobra X19")

    # Passes
    passes_brasilia_x18 = models.IntegerField(verbose_name="Passes Brasília X18")
    passes_brasilia_x19 = models.IntegerField(verbose_name="Passes Brasília X19")
    passes_formosa_x18 = models.IntegerField(verbose_name="Passes Formosa X18")
    passes_formosa_x19 = models.IntegerField(verbose_name="Passes Formosa X19")
    passes_manaus_x18 = models.IntegerField(verbose_name="Passes Manaus X18")
    passes_manaus_x19 = models.IntegerField(verbose_name="Passes Manaus X19")

    # Antena
    antena_brasilia_x18 = models.CharField(max_length=10, choices=CHOICES, verbose_name="Antena Brasília X18")
    antena_brasilia_x19 = models.CharField(max_length=10, choices=CHOICES, verbose_name="Antena Brasília X19")
    antena_formosa_x18 = models.CharField(max_length=10, choices=CHOICES, verbose_name="Antena Formosa X18")
    antena_formosa_x19 = models.CharField(max_length=10, choices=CHOICES, verbose_name="Antena Formosa X19")
    antena_manaus_x18 = models.CharField(max_length=10, choices=CHOICES, verbose_name="Antena Manaus X18")
    antena_manaus_x19 = models.CharField(max_length=10, choices=CHOICES, verbose_name="Antena Manaus X19")

    # Imagens planejadas
    imagens_planejadas_x18 = models.IntegerField(verbose_name="Imagens Planejadas X18")
    imagens_planejadas_x19 = models.IntegerField(verbose_name="Imagens Planejadas X19")

    # Imagens recebidas
    imagens_recebidas_x18 = models.IntegerField(verbose_name="Imagens Recebidas X18")
    imagens_recebidas_x19 = models.IntegerField(verbose_name="Imagens Recebidas X19")

    # Observações
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
        return f"Lessonia - {self.data}"
