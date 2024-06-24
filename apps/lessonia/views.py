from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from .models import Lessonia
from .forms import LessoniaForm
from datetime import timedelta

@login_required
def index(request):
    if not set(request.user.categories.values_list('name', flat=True)).intersection({'lessonia', 'admin'}):
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('post_login_redirect')
    
    today = timezone.now().date()
    briefing = Lessonia.objects.filter(data=today).first()
    briefings = Lessonia.objects.all()

    return render(request, 'lessonia/index.html', {'briefing': briefing, 'briefings': briefings})

@login_required
def new_briefing(request):
    if not set(request.user.categories.values_list('name', flat=True)).intersection({'lessonia', 'admin'}):
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('post_login_redirect')

    if request.method == 'POST':
        form = LessoniaForm(request.POST)
        if form.is_valid():
            briefing = form.save(commit=False)
            if Lessonia.objects.filter(data=briefing.data).exists():
                messages.error(request, 'Já existe um briefing para esta data.')
                return redirect('lessonia:new_briefing')
            briefing.save()
            messages.success(request, 'Briefing criado com sucesso.')
            return redirect('lessonia:index')
        else:
            messages.error(request, 'Erro ao criar o briefing. Por favor, verifique os dados e tente novamente.')
    else:
        form = LessoniaForm()
    
    return render(request, 'lessonia/briefing_diario.html', {'form': form})

@login_required
def edit_briefing(request, pk):
    if not set(request.user.categories.values_list('name', flat=True)).intersection({'lessonia', 'admin'}):
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('post_login_redirect')

    briefing = get_object_or_404(Lessonia, pk=pk)
    if request.method == 'POST':
        form = LessoniaForm(request.POST, instance=briefing)
        if form.is_valid():
            form.save()
            messages.success(request, 'Briefing atualizado com sucesso.')
            return redirect('lessonia:index')
        else:
            messages.error(request, 'Erro ao atualizar o briefing. Por favor, verifique os dados e tente novamente.')
    else:
        form = LessoniaForm(instance=briefing)
    
    return render(request, 'lessonia/edit_briefing_diario.html', {'form': form})

@login_required
def delete_briefing(request, pk):
    if not set(request.user.categories.values_list('name', flat=True)).intersection({'lessonia', 'admin'}):
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('post_login_redirect')
    
    briefing = get_object_or_404(Lessonia, pk=pk)
    briefing.delete()
    messages.success(request, 'Briefing deletado com sucesso.')
    return redirect('lessonia:index')

@login_required
def week_briefings_list(request):
    if not set(request.user.categories.values_list('name', flat=True)).intersection({'lessonia', 'admin'}):
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('post_login_redirect')
    
    briefings = Lessonia.objects.all()
    weeks = {}

    for briefing in briefings:
        year, week, _ = briefing.data.isocalendar()
        if (year, week) not in weeks:
            weeks[(year, week)] = []
        weeks[(year, week)].append(briefing)

    weeks_list = [{'year': year, 'week': week, 'briefings': briefings} for (year, week), briefings in weeks.items()]
    weeks_list.sort(key=lambda x: (x['year'], x['week']), reverse=True)

    return render(request, 'lessonia/week_briefings_list.html', {'weeks': weeks_list})

@login_required
def week_briefings_detail(request, year, week):
    if not set(request.user.categories.values_list('name', flat=True)).intersection({'lessonia', 'admin'}):
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('post_login_redirect')
    
    first_day_of_week = timezone.datetime.strptime(f'{year}-W{week}-1', "%Y-W%W-%w").date()
    last_day_of_week = first_day_of_week + timedelta(days=6)
    days_of_week = [first_day_of_week + timedelta(days=i) for i in range(7)]

    briefings_dict = {day: Lessonia.objects.filter(data=day).first() for day in days_of_week}
    briefings = [(day, briefings_dict.get(day)) for day in days_of_week]

    return render(request, 'lessonia/week_briefings_detail.html', {
        'briefings': briefings, 
        'year': year, 
        'week': week,
        'first_day_of_week': first_day_of_week,
        'last_day_of_week': last_day_of_week
    })


