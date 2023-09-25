from django.core.exceptions import ValidationError
from django import forms
from .models import Usuarios

''' Formulario personalizado SignUp '''
class SignupForm(forms.ModelForm):
    class Meta:   # <-- Meta relaciona el SignupForm con Usuarios
        model = Usuarios # <-- Relación
        fields = ['username', 'email', 'passwd']
    password = forms.CharField(
        widget=forms.PasswordInput,  # <-- Ocultar contraseña
        min_length=8,
        max_length=16,
        label=('Contraseña')  # <-- Simil a 'label' de html   
    )

''' Formulario personalizado Login '''
class LoginForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['username', 'passwd']
    password = forms.CharField(
        widget=forms.PasswordInput,
        min_length=8,
        max_length=16,
        label=('Contraseña')
    )