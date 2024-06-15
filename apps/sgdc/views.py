from django.shortcuts import render
from django.utils import timezone
from .forms import EspacialSegmentForm
from .models import EspacialSegment
from datetime import timedelta

def create_espacial_segment(request):
    today = timezone.now().date()  # Obter a data de hoje no timezone UTC
    briefing = EspacialSegment.objects.filter(data=today).first()
    
    # Definir as variáveis de contexto para o template
    current_date = today
    briefing_start = timezone.now()
    briefing_end = briefing_start + timedelta(days=1)

    if request.method == 'POST':
        if briefing:
            form = EspacialSegmentForm(request.POST, instance=briefing)
        else:
            form = EspacialSegmentForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Dados salvos com sucesso!"
            return render(request, 'sgdc/briefing_diario.html', {
                'form': form,
                'success_message': success_message,
                'current_date': current_date,
                'briefing_start': briefing_start,
                'briefing_end': briefing_end
            })
        else:
            error_message = "Erro ao salvar os dados. Verifique o formulário."
            return render(request, 'sgdc/briefing_diario.html', {
                'form': form,
                'error_message': error_message,
                'current_date': current_date,
                'briefing_start': briefing_start,
                'briefing_end': briefing_end
            })
    else:
        if briefing:
            form = EspacialSegmentForm(instance=briefing)
        else:
            form = EspacialSegmentForm()
    return render(request, 'sgdc/briefing_diario.html', {
        'form': form,
        'current_date': current_date,
        'briefing_start': briefing_start,
        'briefing_end': briefing_end
    })
