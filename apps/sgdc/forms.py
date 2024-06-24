from django import forms
from .models import EspacialSegment

class EspacialSegmentForm(forms.ModelForm):
    class Meta:
        model = EspacialSegment
        fields = [
            'data',
            'plataforma_saude', 'proc_executados', 'alerta_conjuncao',
            'campanha_ranging', 'prox_manobra', 'tempo_eclipse',
            'smc_brasilia', 'smc_rio', 'cmc_brasilia', 'cmc_rio',
            'tcr_brasilia', 'tcr_rio', 'enlaces_ativos', 'qualidade_enlaces',
            'antena_teatro_em_uso', 'observacoes', 'descricao_operacao',
            'infra_critica_brasilia', 'infra_critica_rio', 'gcn_tcr_brasilia',
            'gcn_tcr_rio', 'clima_espacial', 'ssa_sda',
        ]
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'plataforma_saude': forms.Select(attrs={'class': 'circle-select'}, choices=EspacialSegment.CHOICES),
            'proc_executados': forms.Select(attrs={'class': 'circle-select'}, choices=EspacialSegment.CHOICES),
            'alerta_conjuncao': forms.Select(attrs={'class': 'circle-select'}, choices=EspacialSegment.CHOICES),
            'campanha_ranging': forms.Select(attrs={'class': 'circle-select'}, choices=EspacialSegment.CHOICES),
            'smc_brasilia': forms.Select(attrs={'class': 'circle-select'}, choices=EspacialSegment.CHOICES),
            'smc_rio': forms.Select(attrs={'class': 'circle-select'}, choices=EspacialSegment.CHOICES),
            'cmc_brasilia': forms.Select(attrs={'class': 'circle-select'}, choices=EspacialSegment.CHOICES),
            'cmc_rio': forms.Select(attrs={'class': 'circle-select'}, choices=EspacialSegment.CHOICES),
            'tcr_brasilia': forms.Select(attrs={'class': 'circle-select'}, choices=EspacialSegment.CHOICES),
            'tcr_rio': forms.Select(attrs={'class': 'circle-select'}, choices=EspacialSegment.CHOICES),
            'prox_manobra': forms.TextInput(attrs={'class': 'col-6'}),
            'tempo_eclipse': forms.TextInput(attrs={'type': 'time'}),
            'qualidade_enlaces': forms.Select(attrs={'class': 'circle-select'}, choices=EspacialSegment.CHOICES),
            'antena_teatro_em_uso': forms.Select(choices=EspacialSegment.SIM_NAO_CHOICES),
            'enlaces_ativos': forms.TextInput(attrs={'class': 'col-6'}),
            'observacoes': forms.Textarea(attrs={'class': 'col-12'}),
            'descricao_operacao': forms.Textarea(attrs={'class': 'col-12'}),
            'infra_critica_brasilia': forms.Select(attrs={'class': 'rectangle-select'}, choices=EspacialSegment.CHOICES),
            'infra_critica_rio': forms.Select(attrs={'class': 'rectangle-select'}, choices=EspacialSegment.CHOICES),
            'gcn_tcr_brasilia': forms.Select(attrs={'class': 'rectangle-select'}, choices=EspacialSegment.CHOICES),
            'gcn_tcr_rio': forms.Select(attrs={'class': 'rectangle-select'}, choices=EspacialSegment.CHOICES),
            'clima_espacial': forms.Select(attrs={'class': 'rectangle-select'}, choices=EspacialSegment.CHOICES),
            'ssa_sda': forms.Select(attrs={'class': 'rectangle-select'}, choices=EspacialSegment.CHOICES),
        }
