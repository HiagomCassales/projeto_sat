# apps/users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    category = forms.ChoiceField(choices=[(choice[0], choice[1]) for choice in User.CATEGORY_CHOICES if choice[0] != 'admin'])

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'category']
