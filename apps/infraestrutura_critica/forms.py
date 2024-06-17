from django import forms
from .models import InfraestruturaCritica

class InfraestruturaCriticaForm(forms.ModelForm):
    class Meta:
        model = InfraestruturaCritica
        fields = [
            'gmg1_1_brasilia', 'gmg1_1_rio',
            'gmg1_2_brasilia', 'gmg1_2_rio',
            'autonomia1_brasilia', 'autonomia1_rio',
            'ups1_brasilia', 'ups1_rio',
            'gmg2_1_brasilia', 'gmg2_1_rio',
            'gmg2_2_brasilia', 'gmg2_2_rio',
            'autonomia2_brasilia', 'autonomia2_rio',
            'ups2_brasilia', 'ups2_rio',
            'url1_1_brasilia', 'url1_1_rio',
            'url1_2_brasilia', 'url1_2_rio',
            'url2_1_brasilia', 'url2_1_rio',
            'url2_2_brasilia', 'url2_2_rio',
            'combate_incendio_brasilia', 'combate_incendio_rio',
            'observacoes',
        ]
        widgets = {
            'gmg1_1_brasilia': forms.Select(choices=InfraestruturaCritica.CHOICES),
            'gmg1_1_rio': forms.Select(choices=InfraestruturaCritica.CHOICES),
            'gmg1_2_brasilia': forms.Select(choices=InfraestruturaCritica.CHOICES),
            'gmg1_2_rio': forms.Select(choices=InfraestruturaCritica.CHOICES),
            'autonomia1_brasilia': forms.Select(choices=InfraestruturaCritica.CHOICES),
            'autonomia1_rio': forms.Select(choices=InfraestruturaCritica.CHOICES),
            'ups1_brasilia': forms.Select(choices=InfraestruturaCritica.CHOICES),
            'ups1_rio': forms.Select(choices=InfraestruturaCritica.CHOICES),
            'gmg2_1_brasilia': forms.Select(choices=InfraestruturaCritica.CHOICES),
            'gmg2_1_rio': forms.Select(choices=InfraestruturaCritica.CHOICES),
            'gmg2_2_brasilia': forms.Select(choices=InfraestruturaCritica.CHOICES),
            'gmg2_2_rio': forms.Select(choices=InfraestruturaCritica.CHOICES),
            'autonomia2_brasilia': forms.Select(choices=InfraestruturaCritica.CHOICES),
            'autonomia2_rio': forms.Select(choices=InfraestruturaCritica.CHOICES),
            'ups2_brasilia': forms.Select(choices=InfraestruturaCritica.CHOICES),
            'ups2_rio': forms.Select(choices=InfraestruturaCritica.CHOICES),
            'url1_1_brasilia': forms.Select(choices=InfraestruturaCritica.CHOICES),
            'url1_1_rio': forms.Select(choices=InfraestruturaCritica.CHOICES),
            'url1_2_brasilia': forms.Select(choices=InfraestruturaCritica.CHOICES),
            'url1_2_rio': forms.Select(choices=InfraestruturaCritica.CHOICES),
            'url2_1_brasilia': forms.Select(choices=InfraestruturaCritica.CHOICES),
            'url2_1_rio': forms.Select(choices=InfraestruturaCritica.CHOICES),
            'url2_2_brasilia': forms.Select(choices=InfraestruturaCritica.CHOICES),
            'url2_2_rio': forms.Select(choices=InfraestruturaCritica.CHOICES),
            'combate_incendio_brasilia': forms.Select(choices=InfraestruturaCritica.CHOICES),
            'combate_incendio_rio': forms.Select(choices=InfraestruturaCritica.CHOICES),
            'observacoes': forms.Textarea(attrs={'class': 'textarea'}),
        }
