# todos/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User  # ou CustomUser, dependendo do seu modelo

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=255, required=True)
    phone = forms.CharField(max_length=20, required=False)
    birth_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = User
        fields = ['email', 'name', 'password1', 'password2', 'phone', 'birth_date']