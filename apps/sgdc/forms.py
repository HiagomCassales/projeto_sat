from django import forms
from .models import EspacialSegment

class EspacialSegmentForm(forms.ModelForm):
    class Meta:
        model = EspacialSegment
        fields = [
            'plataforma_saude', 'proc_executados', 'alerta_conjuncao',
            'campanha_ranging', 'prox_manobra', 'tempo_eclipse',
            'smc_brasilia', 'smc_rio', 'cmc_brasilia', 'cmc_rio',
            'tcr_brasilia', 'tcr_rio', 'enlaces_ativos', 'qualidade_enlaces',
            'antena_teatro_em_uso'
        ]
        widgets = {
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
        }
