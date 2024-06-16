# apps/sgdc/management/commands/add_specific_data.py
from django.core.management.base import BaseCommand
from apps.sgdc.models import EspacialSegment
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Adiciona dados específicos para segunda-feira, dia 17'

    def handle(self, *args, **kwargs):
        # Data específica para segunda-feira, dia 17
        specific_date = date(2024, 6, 17)

        EspacialSegment.objects.create(
            data=specific_date,
            plataforma_saude="OK",
            proc_executados="OK",
            alerta_conjuncao="NORMAL",
            campanha_ranging="WARN",
            prox_manobra="Manobra G",
            tempo_eclipse=timedelta(hours=7),
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

        self.stdout.write(self.style.SUCCESS('Dados específicos para segunda-feira, dia 17 adicionados com sucesso'))
