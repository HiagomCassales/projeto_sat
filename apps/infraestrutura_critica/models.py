from django.db import models
from django.utils import timezone

class InfraestruturaCritica(models.Model):
    CHOICES = [
        ('NORMAL', 'Normal'),
        ('OK', 'OK'),
        ('WARN', 'Warning'),
        ('CRIT', 'Critical'),
    ]

    data = models.DateField(default=timezone.now, verbose_name="Data")

    # Linha 1 GMG
    gmg1_1_brasilia = models.CharField(max_length=10, choices=CHOICES, verbose_name="GMG 1.1 Brasília")
    gmg1_1_rio = models.CharField(max_length=10, choices=CHOICES, verbose_name="GMG 1.1 Rio de Janeiro")
    gmg1_2_brasilia = models.CharField(max_length=10, choices=CHOICES, verbose_name="GMG 1.2 Brasília")
    gmg1_2_rio = models.CharField(max_length=10, choices=CHOICES, verbose_name="GMG 1.2 Rio de Janeiro")
    autonomia1_brasilia = models.CharField(max_length=10, choices=CHOICES, verbose_name="Autonomia 1 Brasília")
    autonomia1_rio = models.CharField(max_length=10, choices=CHOICES, verbose_name="Autonomia 1 Rio de Janeiro")
    ups1_brasilia = models.CharField(max_length=10, choices=CHOICES, verbose_name="UPS 1 Brasília")
    ups1_rio = models.CharField(max_length=10, choices=CHOICES, verbose_name="UPS 1 Rio de Janeiro")

    # Linha 2 GMG
    gmg2_1_brasilia = models.CharField(max_length=10, choices=CHOICES, verbose_name="GMG 2.1 Brasília")
    gmg2_1_rio = models.CharField(max_length=10, choices=CHOICES, verbose_name="GMG 2.1 Rio de Janeiro")
    gmg2_2_brasilia = models.CharField(max_length=10, choices=CHOICES, verbose_name="GMG 2.2 Brasília")
    gmg2_2_rio = models.CharField(max_length=10, choices=CHOICES, verbose_name="GMG 2.2 Rio de Janeiro")
    autonomia2_brasilia = models.CharField(max_length=10, choices=CHOICES, verbose_name="Autonomia 2 Brasília")
    autonomia2_rio = models.CharField(max_length=10, choices=CHOICES, verbose_name="Autonomia 2 Rio de Janeiro")
    ups2_brasilia = models.CharField(max_length=10, choices=CHOICES, verbose_name="UPS 2 Brasília")
    ups2_rio = models.CharField(max_length=10, choices=CHOICES, verbose_name="UPS 2 Rio de Janeiro")

    # Linha 1 URL
    url1_1_brasilia = models.CharField(max_length=10, choices=CHOICES, verbose_name="URL 1.1 Brasília")
    url1_1_rio = models.CharField(max_length=10, choices=CHOICES, verbose_name="URL 1.1 Rio de Janeiro")
    url1_2_brasilia = models.CharField(max_length=10, choices=CHOICES, verbose_name="URL 1.2 Brasília")
    url1_2_rio = models.CharField(max_length=10, choices=CHOICES, verbose_name="URL 1.2 Rio de Janeiro")

    # Linha 2 URL
    url2_1_brasilia = models.CharField(max_length=10, choices=CHOICES, verbose_name="URL 2.1 Brasília")
    url2_1_rio = models.CharField(max_length=10, choices=CHOICES, verbose_name="URL 2.1 Rio de Janeiro")
    url2_2_brasilia = models.CharField(max_length=10, choices=CHOICES, verbose_name="URL 2.2 Brasília")
    url2_2_rio = models.CharField(max_length=10, choices=CHOICES, verbose_name="URL 2.2 Rio de Janeiro")

    # Combate a Incêndio
    combate_incendio_brasilia = models.CharField(max_length=10, choices=CHOICES, verbose_name="Combate a Incêndio Brasília")
    combate_incendio_rio = models.CharField(max_length=10, choices=CHOICES, verbose_name="Combate a Incêndio Rio de Janeiro")

    # Observações
    observacoes = models.TextField(verbose_name="Observações", blank=True, null=True)

    def __str__(self):
        return f"Infraestrutura Crítica - {self.data}"
