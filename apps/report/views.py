from django.shortcuts import render
from apps.infraestrutura_critica.models import InfraestruturaCritica
from apps.lessonia.models import Lessonia
from apps.sgdc.models import EspacialSegment
from apps.contratos_imagens.models import ContratosImagens
from apps.clima_espacial.models import ClimaEspacial
from django.utils import timezone
from datetime import datetime

def report_view(request):
    data = request.GET.get('data', timezone.now().date().isoformat())
    data = datetime.strptime(data, '%Y-%m-%d').date()

    espacial_segments = EspacialSegment.objects.filter(data=data)
    lessonias = Lessonia.objects.filter(data=data)
    infraestruturas = InfraestruturaCritica.objects.filter(data=data)
    contratos = ContratosImagens.objects.filter(data=data)
    climas = ClimaEspacial.objects.filter(data=data)

    context = {
        'data': data,
        'espacial_segments': espacial_segments,
        'lessonias': lessonias,
        'infraestruturas': infraestruturas,
        'contratos': contratos,
        'climas': climas,
    }

    return render(request, 'report/report.html', context)
