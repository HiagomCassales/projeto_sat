from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from .models import ContratosImagens
from .forms import ContratosImagensForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def index(request):
    if not set(request.user.categories.values_list('name', flat=True)).intersection({'contratos_imagens', 'admin'}):
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('post_login_redirect')
    
    today = timezone.now().date()
    contrato = ContratosImagens.objects.filter(data=today).first()
    contratos = ContratosImagens.objects.all()

    return render(request, 'contratos_imagens/index.html', {'contrato': contrato, 'contratos': contratos})

@login_required
def new_contrato(request):
    if not set(request.user.categories.values_list('name', flat=True)).intersection({'contratos_imagens', 'admin'}):
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('post_login_redirect')
    
    today = timezone.now().date()
    if ContratosImagens.objects.filter(data=today).exists():
        messages.warning(request, 'Um contrato para hoje já existe.')
        return redirect('contratos_imagens:index')
    
    if request.method == 'POST':
        form = ContratosImagensForm(request.POST)
        if form.is_valid():
            contrato = form.save(commit=False)
            contrato.data = today
            contrato.save()
            messages.success(request, 'Contrato criado com sucesso.')
            return redirect('contratos_imagens:index')
        else:
            messages.error(request, 'Erro ao criar o contrato. Por favor, verifique os dados e tente novamente.')
    else:
        form = ContratosImagensForm()
    
    return render(request, 'contratos_imagens/new_contrato.html', {'form': form})

@login_required
def edit_contrato(request, pk):
    if not set(request.user.categories.values_list('name', flat=True)).intersection({'contratos_imagens', 'admin'}):
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('post_login_redirect')
    
    contrato = get_object_or_404(ContratosImagens, pk=pk)
    if request.method == 'POST':
        form = ContratosImagensForm(request.POST, instance=contrato)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contrato atualizado com sucesso.')
            return redirect('contratos_imagens:index')
        else:
            messages.error(request, 'Erro ao atualizar o contrato. Por favor, verifique os dados e tente novamente.')
    else:
        form = ContratosImagensForm(instance=contrato)
    
    return render(request, 'contratos_imagens/edit_contrato.html', {'form': form})

@login_required
def delete_contrato(request, pk):
    if not set(request.user.categories.values_list('name', flat=True)).intersection({'contratos_imagens', 'admin'}):
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('post_login_redirect')
    
    contrato = get_object_or_404(ContratosImagens, pk=pk)
    contrato.delete()
    messages.success(request, 'Contrato deletado com sucesso.')
    return redirect('contratos_imagens:index')
