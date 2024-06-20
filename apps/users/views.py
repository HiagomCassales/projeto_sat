from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import UserRegisterForm
from .models import User, Category

def register(request):
    first_admin = not User.objects.filter(categories__name='admin').exists()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, first_admin=first_admin)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Desativar o usuário até que seja aprovado
            user.save()
            form.save_m2m()  # Salvar as categorias many-to-many
            if first_admin:
                admin_category = Category.objects.get(name='admin')
                user.categories.add(admin_category)
                user.is_active = True
                user.is_approved = True
                messages.success(request, f'Primeiro admin {user.username} criado e ativado.')
            else:
                messages.success(request, f'Conta criada para {user.username}! Aguardando aprovação do administrador.')
            user.save()
            return redirect('login')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = UserRegisterForm(first_admin=first_admin)
    return render(request, 'users/register.html', {'form': form, 'first_admin': first_admin})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_approved:
                auth_login(request, user)
                messages.success(request, 'Login realizado com sucesso.')
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
    categories = user.categories.values_list('name', flat=True)
    if 'admin' in categories:
        return redirect('admin_view')
    elif 'sgdc' in categories:
        return redirect('sgdc:index')
    elif 'lessonia' in categories:
        return redirect('lessonia:index')
    elif 'infraestrutura_critica' in categories:
        return redirect('infraestrutura_critica:index')
    elif 'clima_espacial' in categories:
        return redirect('clima_espacial:index')
    elif 'contratos_imagens' in categories:
        return redirect('contratos_imagens:index')  # Nova linha adicionada aqui
    else:
        messages.error(request, "Categoria de usuário desconhecida.")
        return redirect('login')


@login_required
def admin_view(request):
    if 'admin' not in request.user.categories.values_list('name', flat=True):
        return HttpResponseForbidden()
    pending_users = User.objects.filter(is_approved=False, is_active=False)
    approved_users = User.objects.filter(is_approved=True, is_active=True)
    categories = Category.objects.all()
    is_admin = 'admin' in request.user.categories.values_list('name', flat=True)
    return render(request, 'admin/admin_template.html', {
        'pending_users': pending_users,
        'approved_users': approved_users,
        'categories': categories,
        'is_admin': is_admin,
    })

@login_required
def approve_user(request, user_id):
    if 'admin' not in request.user.categories.values_list('name', flat=True):
        return HttpResponseForbidden()
    user = get_object_or_404(User, id=user_id)
    if 'admin' in user.categories.values_list('name', flat=True) and 'admin' not in request.user.categories.values_list('name', flat=True):
        return HttpResponseForbidden("Apenas administradores podem aprovar outros administradores.")
    user.is_approved = True
    user.is_active = True  # Ativar o usuário após aprovação
    user.save()
    messages.success(request, f'Usuário {user.username} aprovado com sucesso.')
    return redirect('admin_view')

@login_required
def reject_user(request, user_id):
    if 'admin' not in request.user.categories.values_list('name', flat=True):
        return HttpResponseForbidden()
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, f'Usuário {user.username} rejeitado e removido com sucesso.')
    return redirect('admin_view')

@login_required
def delete_user(request, user_id):
    if 'admin' not in request.user.categories.values_list('name', flat=True):
        return HttpResponseForbidden()
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, f'Usuário {user.username} excluído com sucesso.')
    return redirect('admin_view')

@login_required
def change_category(request, user_id):
    if 'admin' not in request.user.categories.values_list('name', flat=True):
        return HttpResponseForbidden()
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        new_category_ids = request.POST.getlist('categories')
        valid_categories = Category.objects.filter(id__in=new_category_ids)
        if valid_categories.count() != len(new_category_ids):
            messages.error(request, 'Uma ou mais categorias são inválidas.')
        else:
            user.categories.set(valid_categories)
            user.save()
            messages.success(request, f'As categorias do usuário {user.username} foram alteradas.')
    return redirect('admin_view')


@login_required
def sgdc_view(request):
    if not set(request.user.categories.values_list('name', flat=True)).intersection({'sgdc', 'admin'}):
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('post_login_redirect')
    return render(request, 'sgdc/index.html')

@login_required
def lessonia_view(request):
    if not set(request.user.categories.values_list('name', flat=True)).intersection({'lessonia', 'admin'}):
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('post_login_redirect')
    return render(request, 'lessonia/index.html')

@login_required
def infraestruturas_criticas_view(request):
    if not set(request.user.categories.values_list('name', flat=True)).intersection({'infraestrutura_critica', 'admin'}):
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('post_login_redirect')
    return render(request, 'infraestrutura_critica/index.html')

@login_required
def clima_espacial_view(request):
    if not set(request.user.categories.values_list('name', flat=True)).intersection({'clima_espacial', 'admin'}):
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('post_login_redirect')
    return render(request, 'clima_espacial/index.html')

@login_required
def contratos_imagens_view(request):
    if not set(request.user.categories.values_list('name', flat=True)).intersection({'contratos_imagens', 'admin'}):
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect('post_login_redirect')
    return render(request, 'contratos_imagens/index.html')


@login_required
def logout_view(request):
    auth_logout(request)
    messages.success(request, 'Logout realizado com sucesso.')
    return redirect('login')
