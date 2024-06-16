from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from apps.users.forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('post_login_redirect')
        else:
            messages.error(request, 'Usuário ou senha incorretos. Tente novamente.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def post_login_redirect(request):
    user = request.user
    if user.category == 'sgdc':
        return redirect('sgdc_view')
    elif user.category == 'lessonia':
        return redirect('lessonia_view')
    elif user.category == 'infraestruturas_criticas':
        return redirect('infraestruturas_criticas_view')
    elif user.category == 'admin':
        return redirect('admin_view')
    else:
        return HttpResponseForbidden("Categoria de usuário desconhecida.")

@login_required
def admin_view(request):
    if request.user.category != 'admin':
        return HttpResponseForbidden()
    return render(request, 'admin/admin_template.html')

@login_required
def sgdc_view(request):
    if request.user.category != 'sgdc' and request.user.category != 'admin':
        return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
    return redirect('index')

@login_required
def lessonia_view(request):
    if request.user.category != 'lessonia' and request.user.category != 'admin':
        return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
    return render(request, 'lessonia/index.html')

@login_required
def infraestruturas_criticas_view(request):
    if request.user.category != 'infraestruturas_criticas' and request.user.category != 'admin':
        return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
    return render(request, 'infraestruturas_criticas/index.html')

@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('login')
