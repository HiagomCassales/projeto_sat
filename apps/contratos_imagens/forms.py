from django import forms
from .models import ContratosImagens

class ContratosImagensForm(forms.ModelForm):
    class Meta:
        model = ContratosImagens
        fields = ['data', 'lote_7_planejado', 'iceye_planejado', 'lote_7_recebido', 'iceye_recebido']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
