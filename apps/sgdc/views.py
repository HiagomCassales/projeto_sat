from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import EspacialSegment
from .forms import EspacialSegmentForm
from datetime import timedelta

def index(request):
    today = timezone.now().date()
    briefing = EspacialSegment.objects.filter(data=today).first()
    briefings = EspacialSegment.objects.all()

    return render(request, 'sgdc/index.html', {'briefing': briefing, 'briefings': briefings})

def new_briefing(request):
    today = timezone.now().date()
    if EspacialSegment.objects.filter(data=today).exists():
        return redirect('index')
    
    if request.method == 'POST':
        form = EspacialSegmentForm(request.POST)
        if form.is_valid():
            briefing = form.save(commit=False)
            briefing.data = today
            briefing.save()
            return redirect('index')
    else:
        form = EspacialSegmentForm()
    
    return render(request, 'sgdc/briefing_diario.html', {'form': form})

def edit_briefing(request, pk):
    briefing = get_object_or_404(EspacialSegment, pk=pk)
    if request.method == 'POST':
        form = EspacialSegmentForm(request.POST, instance=briefing)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EspacialSegmentForm(instance=briefing)
    
    return render(request, 'sgdc/edit_briefing_diario.html', {'form': form})

def delete_briefing(request, pk):
    briefing = get_object_or_404(EspacialSegment, pk=pk)
    briefing.delete()
    return redirect('index')

def week_briefings_list(request):
    briefings = EspacialSegment.objects.all()
    weeks = {}

    for briefing in briefings:
        year, week, _ = briefing.data.isocalendar()
        if (year, week) not in weeks:
            weeks[(year, week)] = []
        weeks[(year, week)].append(briefing)

    weeks_list = [{'year': year, 'week': week, 'briefings': briefings} for (year, week), briefings in weeks.items()]
    weeks_list.sort(key=lambda x: (x['year'], x['week']), reverse=True)

    return render(request, 'sgdc/week_briefings_list.html', {'weeks': weeks_list})

def week_briefings_detail(request, year, week):
    first_day_of_week = timezone.datetime.strptime(f'{year}-W{week}-1', "%Y-W%W-%w").date()
    last_day_of_week = first_day_of_week + timedelta(days=6)
    days_of_week = [first_day_of_week + timedelta(days=i) for i in range(7)]

    briefings_dict = {day: EspacialSegment.objects.filter(data=day).first() for day in days_of_week}
    briefings = [(day, briefings_dict.get(day)) for day in days_of_week]

    return render(request, 'sgdc/week_briefings_detail.html', {
        'briefings': briefings, 
        'year': year, 
        'week': week,
        'first_day_of_week': first_day_of_week,
        'last_day_of_week': last_day_of_week
    })
