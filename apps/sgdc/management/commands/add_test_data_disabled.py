# apps/sgdc/management/commands/add_test_data.py
from django.core.management.base import BaseCommand
from apps.sgdc.models import EspacialSegment
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Adiciona dados fictícios para testes'

    def handle(self, *args, **kwargs):
        today = timezone.now().date()

        data_ficticia = [
            {"data": today - timedelta(days=1), "plataforma_saude": "OK", "proc_executados": "OK", "alerta_conjuncao": "NORMAL", "campanha_ranging": "WARN", "prox_manobra": "Manobra A", "tempo_eclipse": timedelta(hours=1)},
            {"data": today - timedelta(days=2), "plataforma_saude": "WARN", "proc_executados": "WARN", "alerta_conjuncao": "OK", "campanha_ranging": "CRIT", "prox_manobra": "Manobra B", "tempo_eclipse": timedelta(hours=2)},
            {"data": today - timedelta(days=3), "plataforma_saude": "CRIT", "proc_executados": "CRIT", "alerta_conjuncao": "WARN", "campanha_ranging": "NORMAL", "prox_manobra": "Manobra C", "tempo_eclipse": timedelta(hours=3)},
            {"data": today - timedelta(days=4), "plataforma_saude": "NORMAL", "proc_executados": "NORMAL", "alerta_conjuncao": "CRIT", "campanha_ranging": "OK", "prox_manobra": "Manobra D", "tempo_eclipse": timedelta(hours=4)},
            {"data": today - timedelta(days=5), "plataforma_saude": "OK", "proc_executados": "OK", "alerta_conjuncao": "NORMAL", "campanha_ranging": "WARN", "prox_manobra": "Manobra E", "tempo_eclipse": timedelta(hours=5)},
            {"data": today - timedelta(days=6), "plataforma_saude": "WARN", "proc_executados": "WARN", "alerta_conjuncao": "OK", "campanha_ranging": "CRIT", "prox_manobra": "Manobra F", "tempo_eclipse": timedelta(hours=6)},
        ]

        for item in data_ficticia:
            EspacialSegment.objects.create(
                data=item["data"],
                plataforma_saude=item["plataforma_saude"],
                proc_executados=item["proc_executados"],
                alerta_conjuncao=item["alerta_conjuncao"],
                campanha_ranging=item["campanha_ranging"],
                prox_manobra=item["prox_manobra"],
                tempo_eclipse=item["tempo_eclipse"],
                smc_brasilia='OK',
                smc_rio='OK',
                cmc_brasilia='OK',
                cmc_rio='OK',
                tcr_brasilia='OK',
                tcr_rio='OK',
                enlaces_ativos=5,
                qualidade_enlaces='OK',
                antena_teatro_em_uso='NAO',
                descricao_operacao='Operação padrão',
                infra_critica_brasilia='OK',
                infra_critica_rio='OK',
                gcn_tcr_brasilia='OK',
                gcn_tcr_rio='OK',
                clima_espacial='OK',
                ssa_sda='OK'
            )

        self.stdout.write(self.style.SUCCESS('Dados fictícios adicionados com sucesso'))
