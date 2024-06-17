# apps/infraestrutura_critica/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import InfraestruturaCritica
from .forms import InfraestruturaCriticaForm
from datetime import timedelta

@login_required
def index(request):
    if request.user.category != 'infraestrutura_critica' and request.user.category != 'admin':
        return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
    
    today = timezone.now().date()
    briefing = InfraestruturaCritica.objects.filter(data=today).first()
    briefings = InfraestruturaCritica.objects.all()

    return render(request, 'infraestrutura_critica/index.html', {'briefing': briefing, 'briefings': briefings})

@login_required
def new_briefing(request):
    if request.user.category != 'infraestrutura_critica' and request.user.category != 'admin':
        return HttpResponseForbidden("Você não tem permissão para acessar esta página.")

    today = timezone.now().date()
    if InfraestruturaCritica.objects.filter(data=today).exists():
        return redirect('infraestrutura_critica:index')
    
    if request.method == 'POST':
        form = InfraestruturaCriticaForm(request.POST)
        if form.is_valid():
            briefing = form.save(commit=False)
            briefing.data = today
            briefing.save()
            return redirect('infraestrutura_critica:index')
    else:
        form = InfraestruturaCriticaForm()
    
    return render(request, 'infraestrutura_critica/briefing_diario.html', {'form': form})

@login_required
def edit_briefing(request, pk):
    if request.user.category != 'infraestrutura_critica' and request.user.category != 'admin':
        return HttpResponseForbidden("Você não tem permissão para acessar esta página.")

    briefing = get_object_or_404(InfraestruturaCritica, pk=pk)
    if request.method == 'POST':
        form = InfraestruturaCriticaForm(request.POST, instance=briefing)
        if form.is_valid():
            form.save()
            return redirect('infraestrutura_critica:index')
    else:
        form = InfraestruturaCriticaForm(instance=briefing)
    
    return render(request, 'infraestrutura_critica/edit_briefing_diario.html', {'form': form})

@login_required
def delete_briefing(request, pk):
    if request.user.category != 'infraestrutura_critica' and request.user.category != 'admin':
        return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
    
    briefing = get_object_or_404(InfraestruturaCritica, pk=pk)
    briefing.delete()
    return redirect('infraestrutura_critica:index')

@login_required
def week_briefings_list(request):
    if request.user.category != 'infraestrutura_critica' and request.user.category != 'admin':
        return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
    
    briefings = InfraestruturaCritica.objects.all()
    weeks = {}

    for briefing in briefings:
        year, week, _ = briefing.data.isocalendar()
        if (year, week) not in weeks:
            weeks[(year, week)] = []
        weeks[(year, week)].append(briefing)

    weeks_list = [{'year': year, 'week': week, 'briefings': briefings} for (year, week), briefings in weeks.items()]
    weeks_list.sort(key=lambda x: (x['year'], x['week']), reverse=True)

    return render(request, 'infraestrutura_critica/week_briefings_list.html', {'weeks': weeks_list})

@login_required
def week_briefings_detail(request, year, week):
    if request.user.category != 'infraestrutura_critica' and request.user.category != 'admin':
        return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
    
    first_day_of_week = timezone.datetime.strptime(f'{year}-W{week}-1', "%Y-W%W-%w").date()
    last_day_of_week = first_day_of_week + timedelta(days=6)
    days_of_week = [first_day_of_week + timedelta(days=i) for i in range(7)]

    briefings_dict = {day: InfraestruturaCritica.objects.filter(data=day).first() for day in days_of_week}
    briefings = [(day, briefings_dict.get(day)) for day in days_of_week]

    return render(request, 'infraestrutura_critica/week_briefings_detail.html', {
        'briefings': briefings, 
        'year': year, 
        'week': week,
        'first_day_of_week': first_day_of_week,
        'last_day_of_week': last_day_of_week
    })
