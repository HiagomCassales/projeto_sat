from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.utils import timezone
from django.contrib import messages
from .models import BriefingRaoa
from .forms import BriefingRaoaForm
from datetime import timedelta

def has_permission(user):
    return user.is_superuser or user.categories.filter(name='sgdc').exists() or user.categories.filter(name='admin').exists()

@login_required
def index(request):
    if not has_permission(request.user):
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('post_login_redirect')
    
    today = timezone.now().date()
    briefing = BriefingRaoa.objects.filter(data=today).first()
    briefings = BriefingRaoa.objects.all()
    
    return render(request, 'briefing_raoa_sgdc/index.html', {'briefing': briefing, 'briefings': briefings})

@login_required
def new_briefing(request):
    if not has_permission(request.user):
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('post_login_redirect')
    
    today = timezone.now().date()
    if BriefingRaoa.objects.filter(data=today).exists():
        messages.warning(request, 'Um briefing para hoje já existe.')
        return redirect('briefing_raoa_sgdc:index')
    
    if request.method == 'POST':
        form = BriefingRaoaForm(request.POST)
        if form.is_valid():
            briefing = form.save(commit=False)
            briefing.data = today
            briefing.save()
            messages.success(request, 'Briefing criado com sucesso.')
            return redirect('briefing_raoa_sgdc:index')
        else:
            messages.error(request, 'Erro ao criar o briefing. Por favor, verifique os dados e tente novamente.')
    else:
        form = BriefingRaoaForm()
    
    return render(request, 'briefing_raoa_sgdc/briefing_diario.html', {'form': form})

@login_required
def edit_briefing(request, pk):
    if not has_permission(request.user):
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('post_login_redirect')
    
    briefing = get_object_or_404(BriefingRaoa, pk=pk)
    if request.method == 'POST':
        form = BriefingRaoaForm(request.POST, instance=briefing)
        if form.is_valid():
            form.save()
            messages.success(request, 'Briefing atualizado com sucesso.')
            return redirect('briefing_raoa_sgdc:index')
        else:
            messages.error(request, 'Erro ao atualizar o briefing. Por favor, verifique os dados e tente novamente.')
    else:
        form = BriefingRaoaForm(instance=briefing)
    
    return render(request, 'briefing_raoa_sgdc/edit_briefing_diario.html', {'form': form})

@login_required
def delete_briefing(request, pk):
    if not has_permission(request.user):
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('post_login_redirect')
    
    briefing = get_object_or_404(BriefingRaoa, pk=pk)
    briefing.delete()
    messages.success(request, 'Briefing deletado com sucesso.')
    return redirect('briefing_raoa_sgdc:index')

@login_required
def week_briefings_list(request):
    if not has_permission(request.user):
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('post_login_redirect')
    
    briefings = BriefingRaoa.objects.all()
    weeks = {}

    for briefing in briefings:
        year, week, _ = briefing.data.isocalendar()
        if (year, week) not in weeks:
            weeks[(year, week)] = []
        weeks[(year, week)].append(briefing)

    weeks_list = [{'year': year, 'week': week, 'briefings': briefings} for (year, week), briefings in weeks.items()]
    weeks_list.sort(key=lambda x: (x['year'], x['week']), reverse=True)

    return render(request, 'briefing_raoa_sgdc/week_briefings_list.html', {'weeks': weeks_list})

@login_required
def week_briefings_detail(request, year, week):
    if not has_permission(request.user):
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('post_login_redirect')
    
    first_day_of_week = timezone.datetime.strptime(f'{year}-W{week}-1', "%Y-W%W-%w").date()
    last_day_of_week = first_day_of_week + timedelta(days=6)
    days_of_week = [first_day_of_week + timedelta(days=i) for i in range(7)]

    briefings_dict = {day: BriefingRaoa.objects.filter(data=day).first() for day in days_of_week}
    briefings = [(day, briefings_dict.get(day)) for day in days_of_week]

    return render(request, 'briefing_raoa_sgdc/week_briefings_detail.html', {
        'briefings': briefings, 
        'year': year, 
        'week': week,
        'first_day_of_week': first_day_of_week,
        'last_day_of_week': last_day_of_week
    })
