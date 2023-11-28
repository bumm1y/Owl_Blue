import re
from django.core.exceptions import ValidationError
from django import forms
from .models import UsuariosForm, InfoUsuario
from django.core.validators import validate_email

class EdicionPerfilForm(forms.ModelForm):
    class Meta:
        model = InfoUsuario
        fields = ['image']
        widgets = {
            # imágenes precargadas
            'image': forms.Select(choices=[
                ('img/defaultuser.png', 'Foto por defecto'),
                ('img/owlblue_icon.png', 'Icono 1'),
                ('img/owlblue_icon2.png', 'Icono 2'),
                ('img/owlblue_icon3.png', 'Icono 3'),
                ('img/owlblue_icon4.png', 'Icono 4'),
                ('img/owlblue_icon5.png', 'Icono 5'),
            ])
        }

    
''' Formulario personalizado SignUp '''
class SignupForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,  # <-- Ocultar contraseña
        min_length=8,
        max_length=16,
        label=('Contraseña')  # <-- Simil a 'label' de html
        )
    email = forms.EmailField(
        max_length=100,
        required=True,
        label ="Email",
        validators=[validate_email]
    )
    class Meta:   # <-- Meta relaciona el SignupForm con Usuarios
        model = UsuariosForm # <-- Relación
        fields = ['username', 'email', 'passwd']

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username.isalnum(): #Verifica si usuario es alfanumérico
            raise ValidationError('El nombre de usuario solo debe contener letras y números.')
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if not validate_email(email): #Verifica el email 
            raise ValidationError('Ingresa un correo electrónico válido.')
        return email
    
    def clean_password(self):
        contraseña = self.cleaned_data['password']
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,16}$', contraseña): #Verifica las validaciones de la contraseña
            raise ValidationError('La contraseña debe ser de 8 caracteres como mínimo, además de incluir una minúscula, una mayúscula y un número.')
        return contraseña

''' Formulario personalizado Login '''
class LoginForm(forms.ModelForm):
    class Meta:
        model = UsuariosForm
        fields = ['username', 'passwd']
    password = forms.CharField(
        widget=forms.PasswordInput,
        min_length=8,
        max_length=16,
        label=('Contraseña')
    )

