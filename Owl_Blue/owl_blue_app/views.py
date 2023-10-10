from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Categoria
from django.contrib.auth.decorators import login_required

# Página home
def index(request):
    mensaje_confirmacion = request.session.pop('mensaje_confirmacion', None) # <-- Verifica el mensaje de confirmación
    return render(request, 'owl_blue_app/index.html', {'mensaje_confirmacion': mensaje_confirmacion})# <-- 'Carga' la página home y envía el mensaje de confirmación

# Registro de usuarios
def signup(request):
    ''' Traspasa los datos entregados en html al SignupForm'''
    if request.method == 'GET':
        form = SignupForm() # <-- formulario personalizado
        return render(request, 'owl_blue_app/signup.html', {'form' : form}) # <-- 'Carga' la página signup
    else:
        form = SignupForm()
        if request.POST["password1"] == request.POST['password2']: # <-- Autenticación de contraseñas
            try:
                user = User.objects.create_user(email=request.POST['email'],
                username=request.POST['username'], password=request.POST['password1'])
                user.save() # <-- Guardado en BBDD
                login(request, user)
                mensaje_confirmacion = f"¡Usuario creado exitosamente!"
                request.session['mensaje_confirmacion'] = mensaje_confirmacion
                return redirect('home')
            except IntegrityError:
                return render(request, 'owl_blue_app/signup.html', {
            'form': form, 'error': '[!] El usuario o correo ingresado ya existe'})
        return render(request, 'owl_blue_app/signup.html', {
            'form': form, 'error': '[!] Las contraseñas no coinciden.'})


# Login
def signin(request):
    form = LoginForm()
    ''' Si se visita sin autenticarse... '''
    if request.method == 'GET':
        return render(request, 'owl_blue_app/signin.html', {
            'form': form})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST[
            'password'
        ])
        if user is None:
            return render(request, 'owl_blue_app/signin.html', {
                'form': form, 'error': '[!] El usuario o la contraseña son incorrectos.'})
        else:
            login(request, user)
            return redirect('home')
# Logout
def signout(request):
    logout(request)
    return redirect('home') 

''' Actividades() '''

@login_required # Se necesita estar logeado para ingresar a actividades
def acts(request):
    acts = Categoria.objects.all()
    return render(request, 'owl_blue_app/acts.html', {
        'acts': acts})


""" Vista cuenta """
@login_required
def myaccount(request):
    return render(request, 'owl_blue_app/myaccount.html')