from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from .models import ClimaEspacial
from .forms import ClimaEspacialForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def index(request):
    if not set(request.user.categories.values_list('name', flat=True)).intersection({'clima_espacial', 'admin'}):
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('post_login_redirect')
    
    today = timezone.now().date()
    briefing = ClimaEspacial.objects.filter(data=today).first()
    briefings = ClimaEspacial.objects.all()

    return render(request, 'clima_espacial/index.html', {'briefing': briefing, 'briefings': briefings})

def new_clima(request):
    if not set(request.user.categories.values_list('name', flat=True)).intersection({'clima_espacial', 'admin'}):
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('post_login_redirect')

    if request.method == 'POST':
        form = ClimaEspacialForm(request.POST)
        if form.is_valid():
            briefing = form.save(commit=False)
            if ClimaEspacial.objects.filter(data=briefing.data).exists():
                messages.error(request, 'Já existe um briefing para esta data.')
                return redirect('clima_espacial:new_clima')
            briefing.save()
            messages.success(request, 'Briefing criado com sucesso.')
            return redirect('clima_espacial:index')
        else:
            messages.error(request, 'Erro ao criar o briefing. Por favor, verifique os dados e tente novamente.')
    else:
        form = ClimaEspacialForm()
    
    return render(request, 'clima_espacial/new_clima.html', {'form': form})

@login_required
def edit_clima(request, pk):
    if not set(request.user.categories.values_list('name', flat=True)).intersection({'clima_espacial', 'admin'}):
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('post_login_redirect')
    
    briefing = get_object_or_404(ClimaEspacial, pk=pk)
    if request.method == 'POST':
        form = ClimaEspacialForm(request.POST, instance=briefing)
        if form.is_valid():
            form.save()
            messages.success(request, 'Briefing atualizado com sucesso.')
            return redirect('clima_espacial:index')
        else:
            messages.error(request, 'Erro ao atualizar o briefing. Por favor, verifique os dados e tente novamente.')
    else:
        form = ClimaEspacialForm(instance=briefing)
    
    return render(request, 'clima_espacial/edit_clima.html', {'form': form})

@login_required
def delete_clima(request, pk):
    if not set(request.user.categories.values_list('name', flat=True)).intersection({'clima_espacial', 'admin'}):
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('post_login_redirect')
    
    briefing = get_object_or_404(ClimaEspacial, pk=pk)
    briefing.delete()
    messages.success(request, 'Briefing deletado com sucesso.')
    return redirect('clima_espacial:index')
