# briefing_raoa_sgdc/forms.py

from django import forms
from .models import BriefingRaoa

class BriefingRaoaForm(forms.ModelForm):
    class Meta:
        model = BriefingRaoa
        fields = [
            'descricao_operacao', 'infra_critica_brasilia', 'infra_critica_rio',
            'gcn_tcr_brasilia', 'gcn_tcr_rio', 'clima_espacial', 'ssa_sda',
        ]
        widgets = {
            'descricao_operacao': forms.Textarea(attrs={'class': 'col-12'}),
            'infra_critica_brasilia': forms.Select(attrs={'class': 'rectangle-select'}, choices=BriefingRaoa.CHOICES),
            'infra_critica_rio': forms.Select(attrs={'class': 'rectangle-select'}, choices=BriefingRaoa.CHOICES),
            'gcn_tcr_brasilia': forms.Select(attrs={'class': 'rectangle-select'}, choices=BriefingRaoa.CHOICES),
            'gcn_tcr_rio': forms.Select(attrs={'class': 'rectangle-select'}, choices=BriefingRaoa.CHOICES),
            'clima_espacial': forms.Select(attrs={'class': 'rectangle-select'}, choices=BriefingRaoa.CHOICES),
            'ssa_sda': forms.Select(attrs={'class': 'rectangle-select'}, choices=BriefingRaoa.CHOICES),
        }
