# apps/users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Category, Contato

class UserRegisterForm(UserCreationForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.none(),
        required=True,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'categories']

    def __init__(self, *args, **kwargs):
        first_admin = kwargs.pop('first_admin', False)
        super().__init__(*args, **kwargs)
        if first_admin:
            self.fields['categories'].queryset = Category.objects.filter(name='admin')
        else:
            self.fields['categories'].queryset = Category.objects.exclude(name='admin')

        # Adiciona classes do Bootstrap aos campos do formulário
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['categories'].widget.attrs.update({'class': 'form-check-input'})

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'numero']

