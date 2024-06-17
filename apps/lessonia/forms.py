from django import forms
from .models import Lessonia

class LessoniaForm(forms.ModelForm):
    class Meta:
        model = Lessonia
        fields = [
            'saude_plataforma_x18', 'saude_plataforma_x19',
            'alerta_conjuncao_x18', 'alerta_conjuncao_x19',
            'manobra_x18', 'manobra_x19',
            'passes_brasilia_x18', 'passes_brasilia_x19',
            'passes_formosa_x18', 'passes_formosa_x19',
            'passes_manaus_x18', 'passes_manaus_x19',
            'antena_brasilia_x18', 'antena_brasilia_x19',
            'antena_formosa_x18', 'antena_formosa_x19',
            'antena_manaus_x18', 'antena_manaus_x19',
            'imagens_planejadas_x18', 'imagens_planejadas_x19',
            'imagens_recebidas_x18', 'imagens_recebidas_x19',
            'observacoes', 'descricao_operacao',
            'infra_critica_brasilia', 'infra_critica_rio', 'gcn_tcr_brasilia',
            'gcn_tcr_rio', 'clima_espacial', 'ssa_sda',
        ]
        widgets = {
            'saude_plataforma_x18': forms.Select(attrs={'class': 'circle-select'}, choices=Lessonia.CHOICES),
            'saude_plataforma_x19': forms.Select(attrs={'class': 'circle-select'}, choices=Lessonia.CHOICES),
            'alerta_conjuncao_x18': forms.Select(attrs={'class': 'circle-select'}, choices=Lessonia.CHOICES),
            'alerta_conjuncao_x19': forms.Select(attrs={'class': 'circle-select'}, choices=Lessonia.CHOICES),
            'manobra_x18': forms.Select(attrs={'class': 'circle-select'}, choices=Lessonia.SIM_NAO_CHOICES),
            'manobra_x19': forms.Select(attrs={'class': 'circle-select'}, choices=Lessonia.SIM_NAO_CHOICES),
            'passes_brasilia_x18': forms.NumberInput(attrs={'class': 'number-input'}),
            'passes_brasilia_x19': forms.NumberInput(attrs={'class': 'number-input'}),
            'passes_formosa_x18': forms.NumberInput(attrs={'class': 'number-input'}),
            'passes_formosa_x19': forms.NumberInput(attrs={'class': 'number-input'}),
            'passes_manaus_x18': forms.NumberInput(attrs={'class': 'number-input'}),
            'passes_manaus_x19': forms.NumberInput(attrs={'class': 'number-input'}),
            'antena_brasilia_x18': forms.Select(attrs={'class': 'circle-select'}, choices=Lessonia.CHOICES),
            'antena_brasilia_x19': forms.Select(attrs={'class': 'circle-select'}, choices=Lessonia.CHOICES),
            'antena_formosa_x18': forms.Select(attrs={'class': 'circle-select'}, choices=Lessonia.CHOICES),
            'antena_formosa_x19': forms.Select(attrs={'class': 'circle-select'}, choices=Lessonia.CHOICES),
            'antena_manaus_x18': forms.Select(attrs={'class': 'circle-select'}, choices=Lessonia.CHOICES),
            'antena_manaus_x19': forms.Select(attrs={'class': 'circle-select'}, choices=Lessonia.CHOICES),
            'imagens_planejadas_x18': forms.NumberInput(attrs={'class': 'number-input'}),
            'imagens_planejadas_x19': forms.NumberInput(attrs={'class': 'number-input'}),
            'imagens_recebidas_x18': forms.NumberInput(attrs={'class': 'number-input'}),
            'imagens_recebidas_x19': forms.NumberInput(attrs={'class': 'number-input'}),
            'observacoes': forms.Textarea(attrs={'class': 'textarea'}),
            'descricao_operacao': forms.Textarea(attrs={'class': 'col-12'}),
            'infra_critica_brasilia': forms.Select(attrs={'class': 'rectangle-select'}, choices=Lessonia.CHOICES),
            'infra_critica_rio': forms.Select(attrs={'class': 'rectangle-select'}, choices=Lessonia.CHOICES),
            'gcn_tcr_brasilia': forms.Select(attrs={'class': 'rectangle-select'}, choices=Lessonia.CHOICES),
            'gcn_tcr_rio': forms.Select(attrs={'class': 'rectangle-select'}, choices=Lessonia.CHOICES),
            'clima_espacial': forms.Select(attrs={'class': 'rectangle-select'}, choices=Lessonia.CHOICES),
            'ssa_sda': forms.Select(attrs={'class': 'rectangle-select'}, choices=Lessonia.CHOICES),
        }
