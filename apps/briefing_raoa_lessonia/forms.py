# briefing_raoa_sgdc/forms.py

from django import forms
from .models import BriefingRaoaLessoniaModels

class BriefingRaoaLessoniaForm(forms.ModelForm):
    class Meta:
        model = BriefingRaoaLessoniaModels
        fields = [
            'descricao_operacao', 'infra_critica_brasilia', 'infra_critica_rio',
            'gcn_tcr_brasilia', 'gcn_tcr_rio', 'clima_espacial', 'ssa_sda',
        ]
        widgets = {
            'descricao_operacao': forms.Textarea(attrs={'class': 'col-12'}),
            'infra_critica_brasilia': forms.Select(attrs={'class': 'rectangle-select'}, choices=BriefingRaoaLessoniaModels.CHOICES),
            'infra_critica_rio': forms.Select(attrs={'class': 'rectangle-select'}, choices=BriefingRaoaLessoniaModels.CHOICES),
            'gcn_tcr_brasilia': forms.Select(attrs={'class': 'rectangle-select'}, choices=BriefingRaoaLessoniaModels.CHOICES),
            'gcn_tcr_rio': forms.Select(attrs={'class': 'rectangle-select'}, choices=BriefingRaoaLessoniaModels.CHOICES),
            'clima_espacial': forms.Select(attrs={'class': 'rectangle-select'}, choices=BriefingRaoaLessoniaModels.CHOICES),
            'ssa_sda': forms.Select(attrs={'class': 'rectangle-select'}, choices=BriefingRaoaLessoniaModels.CHOICES),
        }
