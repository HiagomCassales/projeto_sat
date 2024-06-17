# apps/users/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import UserRegisterForm
from .models import User

from django.contrib.auth import get_user_model

User = get_user_model()

def register(request):
    first_admin = not User.objects.filter(category='admin').exists()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Desativar o usuário até que seja aprovado
            # Permitir o primeiro administrador se não houver nenhum na base de dados
            if first_admin:
                user.category = 'admin'
                user.is_active = True
                user.is_approved = True
                messages.success(request, f'Primeiro admin {user.username} criado e ativado.')
            user.save()
            if user.category != 'admin':
                messages.success(request, f'Conta criada para {user.username}! Aguardando aprovação do administrador.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'first_admin': first_admin})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_approved:
                auth_login(request, user)
                return redirect('post_login_redirect')
            else:
                messages.error(request, 'Sua conta ainda não foi aprovada pelo administrador.')
        else:
            messages.error(request, 'Usuário ou senha incorretos. Tente novamente.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def post_login_redirect(request):
    user = request.user
    if user.category == 'sgdc':
        return redirect('sgdc:index')
    elif user.category == 'lessonia':
        return redirect('lessonia:index')
    elif user.category == 'infraestrutura_critica':
        return redirect('infraestrutura_critica:index')
    elif user.category == 'admin':
        return redirect('admin_view')
    else:
        return HttpResponseForbidden("Categoria de usuário desconhecida.")

@login_required
def admin_view(request):
    if request.user.category != 'admin':
        return HttpResponseForbidden()
    pending_users = User.objects.filter(is_approved=False, is_active=False)
    approved_users = User.objects.filter(is_approved=True, is_active=True)
    return render(request, 'admin/admin_template.html', {
        'pending_users': pending_users,
        'approved_users': approved_users,
    })

@login_required
def approve_user(request, user_id):
    if request.user.category != 'admin':
        return HttpResponseForbidden()
    user = get_object_or_404(User, id=user_id)
    if user.category == 'admin' and request.user.category != 'admin':
        return HttpResponseForbidden("Apenas administradores podem aprovar outros administradores.")
    user.is_approved = True
    user.is_active = True  # Ativar o usuário após aprovação
    user.save()
    messages.success(request, f'Usuário {user.username} aprovado com sucesso.')
    return redirect('admin_view')

@login_required
def reject_user(request, user_id):
    if request.user.category != 'admin':
        return HttpResponseForbidden()
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, f'Usuário {user.username} rejeitado e removido com sucesso.')
    return redirect('admin_view')

@login_required
def delete_user(request, user_id):
    if request.user.category != 'admin':
        return HttpResponseForbidden()
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, f'Usuário {user.username} excluído com sucesso.')
    return redirect('admin_view')

@login_required
def change_category(request, user_id):
    if request.user.category != 'admin':
        return HttpResponseForbidden()
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        new_category = request.POST.get('category')
        if new_category not in dict(User.CATEGORY_CHOICES).keys():
            messages.error(request, 'Categoria inválida.')
        else:
            user.category = new_category
            user.save()
            messages.success(request, f'A categoria do usuário {user.username} foi alterada para {user.get_category_display()}.')
    return redirect('admin_view')

@login_required
def sgdc_view(request):
    if request.user.category != 'sgdc' and request.user.category != 'admin':
        return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
    return redirect('sgdc:index')

@login_required
def lessonia_view(request):
    if request.user.category != 'lessonia' and request.user.category != 'admin':
        return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
    return redirect('lessonia:index')

@login_required
def infraestruturas_criticas_view(request):
    if request.user.category != 'infraestrutura_critica' and request.user.category != 'admin':
        return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
    return redirect('infraestrutura_critica:index')

@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('login')
