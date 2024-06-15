# users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    category = forms.ChoiceField(choices=User.CATEGORY_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'category']
