from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Categoria, Explicaciones, Actividades
from django.contrib.auth.decorators import login_required

''' Cápsula 0 '''
def capsula0(request, categoria_elegida):
    explicaciones = list(Explicaciones.objects.filter(categoria__categoria=categoria_elegida))
    return render(request, 'owl_blue_app/capsula0.html', {'categoria_elegida': categoria_elegida, 'explicaciones': explicaciones})


''' Prueba lessons.html '''
def lessons(request, categoria_elegida):
    categoria = categoria_elegida
    actividades = list(Actividades.objects.filter(categoria__categoria=categoria))
    return render(request, 'owl_blue_app/lessons.html', {'categoria': categoria, 'actividades': actividades})

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
        'form': form, 'error': 'El usuario o correo ingresado ya existe.'})

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
                'form': form, 'error': 'El usuario o la contraseña son incorrectos.'})
        else:
            mensaje_confirmacion = f"Bienvenido de vuelta!"
            request.session['mensaje_confirmacion'] = mensaje_confirmacion
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

@login_required
def abc(request):
    categoria_elegida="Abecedario"
    return render(request, 'owl_blue_app/abc.html', {'categoria_elegida': categoria_elegida})

@login_required
def preguntas(request):
    return render(request, 'owl_blue_app/preguntas.html', {
        'preguntas': preguntas
    })

@login_required
def emociones(request):
    return render(request, 'owl_blue_app/emociones.html', {
        'emociones': emociones
    })

@login_required
def familia(request):
    return render(request, 'owl_blue_app/familia.html', {
        'familia': familia
    })

""" Vista cuenta """
@login_required
def myaccount(request):
    return render(request, 'owl_blue_app/myaccount.html')