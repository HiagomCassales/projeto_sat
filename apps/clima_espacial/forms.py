from django import forms
from .models import ClimaEspacial

class ClimaEspacialForm(forms.ModelForm):
    class Meta:
        model = ClimaEspacial
        fields = ['data', 'maior_k_24h', 'maior_k_previsto', 'tempestade_solar_prevista']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'maior_k_24h': forms.NumberInput(attrs={'class': 'col-6'}),
            'maior_k_previsto': forms.NumberInput(attrs={'class': 'col-6'}),
            'tempestade_solar_prevista': forms.Select(attrs={'class': 'rectangle-select'}, choices=ClimaEspacial.SIM_NAO_CHOICES),
        }
